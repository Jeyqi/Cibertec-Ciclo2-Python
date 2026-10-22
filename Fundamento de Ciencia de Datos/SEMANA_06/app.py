
import streamlit as st 
import pandas as pd 

st.set_page_config(
    page_title="Educa Peru -Evaluacion de Becas",
    page_icon=" ♥",
    layout="wide"
)

st.title("Educa Peru Evaluaciones de Beca")
st.write(
    "Sistema academico demostracion para comprender"
    "la etica , la transparencia, la equidad y la "
    "responsabilidad en la ciencias de Datos"
)

st.info(
    "Este proyecto utilza datos ficticios"
    "No introduzcas datos persnales reales"
)

NOTA_MINIMA=14
INGRESO_MAXIMO=1500
ASISTENCIA_MINIMA=85

st.subheader("1. Criterios de Evaluacion")

col1,col2,col3=st.columns(3)

col1.metric("Nota minima",f"{NOTA_MINIMA}/20")
col2.metric("Ingreso familiar maximo",f"S/ {INGRESO_MAXIMO}")
col3.metric("Asistencia minima",f"{ASISTENCIA_MINIMA}%")

st.caption(
    "Los umbrales son reglas de ejemplo que una isntitucion "
    "real tendria que justificar y validar"
)

datos={
    "Codigo":["EST-001","EST-002","EST-003","EST-004","EST-005"],
    "Nota":[17,15,13,18,16],
    "Ingreso_Familiar":[1200,1800,900,1400,1500],
    "Asistencia":[95,90,92,80,88]
}

df=pd.DataFrame(datos)


def evaluar_beca(fila):
    razones=[]
    if fila["Nota"]<NOTA_MINIMA:
        razones.append(
            f"Nota menor que {NOTA_MINIMA}"
        )
    if fila["Ingreso_Familiar"]>INGRESO_MAXIMO:
        razones.append(
            "Ingreso familiar superior al limite"
        )
    if fila["Asistencia"]<ASISTENCIA_MINIMA:
        razones.append(
            f"Asistencia menor que {ASISTENCIA_MINIMA}%"
        )
        
    if len(razones)==0:
        resultado="Cumple los criterios"
        explicacion=(
            "Cumple la nota, el ingreso familiar"
            "y la asistencia establecidos"
        )
    else:
        resultado="Requiere revision"
        explicacion="; ".join(razones)
        
    return pd.Series({
        "Resultado":resultado,
        "Explicacion":explicacion
    })
    
#apliCaCION DE EVALUACION FILA

evaluaciones=df.apply(evaluar_beca,axis=1)

df_resultados=pd.concat(
    [df,evaluaciones],
    axis=1
)

#resultados de forma transparente

st.subheader("2. Resultados de la evaluacion")

st.write(
    "La siguiente tabla muestras los criterios  y la razones "
    "de cada resultado para facilitar su comprension"
)

st.dataFrame(
    df_resultados,
    use_container_width=True,
    hide_index=True
)

#revision del caso

st.subheader("3. Revision de una solicitud")

codigo_seleccionado=st.selectbox(
    "Seleccion una solicitud para revisar ",
    df_resultados["Codigo"].to_list()
)

caso=df_resultados[
    df_resultados["Codigo"]==codigo_seleccionado
].iloc[0]

st.write(f"**Solicitud: {caso['Codigo']}")
st.write(f"**Resultado: {caso['Resultado']}")
st.write(f"**Motivo: {caso['Explicacion']}")

#Aplico la responsabilidad

st.subheader("4. Revision responsable")
st.write(
    "Una persona autorizadadebe revisar los casos"
    "que puedn contener errores o necesitar una "
    "evaluacion adicional"
)

revision=st.checkbox(
    "Simular que una persona autorizada reviso el caso"
)

if revision:
    st.success(
        "Revision simulada registrada en esta sesion"
        "En este ejemplo no se guarda ningun expediente"
        "ni se concede una beca automaticamente"
    )
else:
    st.warning(
        "el caso aun no ha sido marcado como reisado"
    )
    
#EXPLICAR LOS PRINCIPIOS ETICOS

st.subheader("5. Principios eticos aplicados")

with st.expander("Transparencia"):
    st.write(
             "Se publican los criterios y se explican las razones"
             "de cada resultado , asi el estudiante puede"
             "comprender como se evaluo su solicitud"
    )
with st.expander("Equidad"):
    st.write(
             "Todos los casos utilizan los  mismos criterios"
             "No se utilizan el genero , la religion ni otros"
             "atributos personales irrelevantes para decidir"
    )
    
with st.expander("Responsabilidad"):
    st.write(
             "Una persona autorizada debe supervisar el proceso"
             "corregir errores y revisar los casos cuestinados"
    )

with st.expander("Privacidad"):
    st.write(
             "Se utilizan codigos en vez de nombres y se limita"
             "la informacion mostrada, en un sistema real se "
             "requiere controles de acceso y almacenamiento seguro"
    )

with st.expander("Gobernanza de datos"):
    st.write(
             "La institucion debe definir quien puede acceder,"
             "actualizar y consultar los datos , durante  cuanto"
             "tiempo se conservan y como se corregin los errores..."
    )
    
#mostrar el mensaje final

st.divider()

st.success(
    
    "Demostracion finalizada, los datos evaluan "
    "Con criterios visibles y explicaciones comprenbsibles"
)

st.caption(
    "Prototipo educativo no es un sistema oficial"
    "de adjudicacion de becas"
)