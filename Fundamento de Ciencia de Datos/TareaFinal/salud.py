import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Salud Perú - Control de Acceso y Privacidad",
    page_icon="🏥",
    layout="wide"
)

st.title("Clínica Salud Perú: Sistema de Gobernanza y Privacidad de Datos")
st.write(
    "Sistema de demostración para gestionar el control de acceso basado en roles (RBAC), "
    "la protección de datos sensibles de pacientes y la trazabilidad de consultas médicas."
)

st.info(
    "Aviso: Este proyecto utiliza datos ficticios para ilustrar políticas de privacidad "
    "y cumplimiento normativo en el sector salud."
)

# 1. Definición de Roles y Permisos (Control de Acceso)
st.subheader("1. Control de Acceso Basado en Roles (RBAC)")
st.write("Seleccione el rol del trabajador para evaluar cómo cambian los permisos de visualización de datos:")

rol_usuario = st.selectbox(
    "Seleccione su rol en la clínica",
    ["Administrativo General", "Personal de Admisión", "Médico Tratante"]
)

# Base de datos ficticia de pacientes de la clínica
datos = {
    "Codigo_Paciente": ["PAC-001", "PAC-002", "PAC-003", "PAC-004"],
    "Nombre": ["Juan Pérez", "María Gómez", "Carlos Ruiz", "Ana Torres"],
    "Documento": ["45871293", "71293845", "09831245", "62514389"],
    "Telefono": ["987654321", "912345678", "923456789", "934567891"],
    "Especialidad_Cita": ["Cardiología", "Pediatría", "Medicina General", "Neurología"]
}

df_original = pd.DataFrame(datos)

# Copiamos el DataFrame para aplicar reglas de enmascaramiento según el rol
df_visible = df_original.copy()

if rol_usuario == "Administrativo General":
    # El personal administrativo no debe ver documentos ni teléfonos sensibles
    df_visible["Documento"] = "[OCULTO - Sin Privilegios]"
    df_visible["Telefono"] = "[OCULTO - Sin Privilegios]"
    st.warning("⚠️ Acceso Restringido: Como Administrativo General, la información de contacto y documentos está enmascarada por privacidad.")

elif rol_usuario == "Personal de Admisión":
    # Admisión ve parcialmente los documentos necesarios para coordinar citas, pero oculta detalles médicos profundos
    df_visible["Documento"] = df_visible["Documento"].apply(lambda x: x[:4] + "****")
    st.info("ℹ️ Acceso Parcial: Personal de admisión con visualización limitada de documentos de identidad.")

else:
    st.success("✅ Acceso Completo: Médico Tratante autorizado para ver datos completos de identificación y citas.")

# 2. Mostrar la tabla de resultados protegida
st.subheader("2. Registro de Pacientes y Citas (Vista Filtrada)")
st.write("La tabla muestra únicamente los campos permitidos según el nivel de autorización del rol seleccionado.")

st.dataframe(
    df_visible,
    use_container_width=True,
    hide_index=True
)

# 3. Simulación de Auditoría y Registro de Consultas (Responsabilidad y Trazabilidad)
st.subheader("3. Auditoría y Trazabilidad de Consultas")
st.write("Para evitar accesos indebidos, cada consulta a expedientes médicos queda registrada en un sistema de logs.")

registrar_auditoria = st.checkbox(
    "Registrar esta consulta en el sistema de auditoría interna"
)

if registrar_auditoria:
    st.success(
        f"✔️ Auditoría registrada: El rol '{rol_usuario}' consultó los registros "
        f"de pacientes de forma exitosa en la sesión actual."
    )
else:
    st.warning(
        "⚠️ La consulta no ha sido marcada para auditoría detallada en este momento."
    )

# 4. Principios de Privacidad y Gobernanza de Datos Aplicados
st.subheader("4. Principios de Privacidad y Gobernanza Aplicados")

with st.expander("Control de Acceso Basado en Roles (RBAC)"):
    st.write(
        "Se limita la visualización de datos sensibles según las funciones estrictas del trabajador. "
        "Un colaborador administrativo no requiere consultar números de documentos completos ni teléfonos personales de los pacientes."
    )

with st.expander("Minimización de Datos"):
    st.write(
        "El sistema recopila y expone únicamente la información indispensable para cumplir con la tarea operativa requerida, "
        "reduciendo drásticamente el riesgo de filtraciones."
    )

with st.expander("Trazabilidad y Responsabilidad"):
    st.write(
        "La capacidad de auditar quién accede a qué información establece responsabilidades claras y disuade "
        "a los trabajadores de realizar consultas indebidas fuera de su ámbito laboral."
    )

with st.expander("Privacidad desde el Diseño"):
    st.write(
        "La protección de datos personales y médicos está integrada directamente en la arquitectura del software, "
        "ocultando la información confidencial de manera automatizada."
    )

# Mensaje final
st.divider()
st.success(
    "Demostración de gobernanza de datos en la Clínica Salud Perú finalizada con éxito."
)
st.caption(
    "Prototipo educativo enfocado en la ciberseguridad, privacidad de datos y ética en Ciencia de Datos."
)