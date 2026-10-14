# CustomerVoice AI

Sistema de evaluación de satisfacción del cliente que combina una **nota numérica (1-10)** con el **análisis de sentimiento del comentario** mediante un modelo Transformer de Hugging Face. Persiste todo en SQLite3 y genera alertas cuando la nota contradice lo que dice el cliente.

Curso: Lenguaje de Ciencia de Datos I — Cibertec, 2026-II

## Estructura

```
customervoice-ai/
├── main.py           Ejecuta el flujo completo (carga, análisis, reporte, evaluación)
├── menu.py           Menú interactivo para operar el sistema (CRUD manual)
├── ingesta.py        Módulo 1: lectura y validación del CSV
├── modelo_ia.py      Módulo 2: análisis de sentimiento y regla del flag
├── db.py             Módulo 3: base de datos SQLite3 y operaciones CRUD
├── reportes.py       Módulo 4: reporte ejecutivo en TXT
├── evaluacion.py     Métricas del modelo contra las etiquetas manuales
├── requirements.txt
├── data/
│   └── evaluaciones_clientes.csv
└── reportes/         Aquí se guardan los reportes generados
```

## Instalación (Windows)

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

La primera ejecución descarga el modelo (~435 MB), que queda en caché para las siguientes.

## Uso

```powershell
python main.py   # carga el CSV, analiza los 120 comentarios y genera los reportes
python menu.py   # registrar, listar, modificar o eliminar evaluaciones
```

`main.py` recarga la base desde cero en cada ejecución.

## Flujo

```
CSV → validación → SQLite → modelo de IA → SQLite (UPDATE) → reporte TXT + evaluación
```

## Componentes técnicos

**Modelo:** `pysentimiento/robertuito-sentiment-analysis` (español, clases POS / NEG / NEU). Se eligió frente a `cardiffnlp/twitter-xlm-roberta-base-sentiment` porque en una prueba de 20 frases obtuvo 95% contra 80%, y el segundo falló en los 3 casos de sarcasmo.

**Base de datos:** dos tablas relacionadas.

| Tabla | Columnas |
|---|---|
| `clientes` | `cliente_id` (PK) |
| `evaluaciones` | `id` (PK), `cliente_id` (FK), `fecha`, `nota` (CHECK 1-10), `comentario`, `sentimiento_real`, `sentimiento_modelo`, `score`, `flag` |

**Operaciones:** DDL (`CREATE TABLE`) y DML (`INSERT`, `SELECT`, `UPDATE`, `DELETE`), todas en `db.py`.

**Validación de ingesta:** se descartan filas con nota no numérica o fuera de 1-10, fecha inválida, comentario vacío o etiqueta desconocida, indicando el número de fila y el motivo.

**Regla de incongruencia (flag = 1):**
- nota 9-10 y comentario negativo, o
- nota 1-4 y comentario positivo.

## Resultados (dataset de 120 evaluaciones)

| Métrica | Resultado |
|---|---|
| Acierto de sentimiento | **86.7%** (meta: > 85%) |
| Incongruencias detectadas | **16 de 16** (recall 100%) |
| Alertas falsas | 1 (precisión del flag 94.1%) |

Matriz de confusión (filas = real, columnas = modelo):

|  | NEG | NEU | POS |
|---|---|---|---|
| **NEG** | 45 | 6 | 0 |
| **NEU** | 1 | 16 | 3 |
| **POS** | 1 | 5 | 43 |

**Observaciones:**
- Casi todos los errores son confusiones con NEU: quejas sin palabras emocionales ("El producto vino usado") y elogios discretos ("Todo llegó completo y bien embalado").
- La polaridad casi nunca se invierte (1 caso en 120). Eso es lo que importa para el flag.
- Única alerta falsa: "Me devolvieron el dinero rapidísimo, muy serios" (nota 9), clasificado como NEG.
- El score sirve para **ordenar** las alertas, no para descartarlas: el sarcasmo real "Claro, excelente servicio... si te gusta que te ignoren" tuvo la confianza más baja (0.68).

Los resultados se regeneran en `reportes/evaluacion_AAAA-MM-DD.txt` cada vez que se ejecuta `main.py`. Si se modifican las etiquetas del CSV, los números pueden cambiar.
