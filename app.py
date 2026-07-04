import streamlit as st

# 1. Crear las pestañas al principio de todo el código
tab1, tab2 = st.tabs(["📊 Sistema de Monitoreo", "📈 Módulo de Análisis"])

with tab1:
    # AQUÍ DEJAS TODO EL CÓDIGO QUE YA TIENE TU APP.PY ACTUAL
    st.title("Tu app de monitoreo actual...") 
    # (Todo tu código original va aquí adentro, movido un espacio/indentación a la derecha)

with tab2:
    # AQUÍ PEGAS EL CÓDIGO DE TU SEGUNDA APP
    st.title("Módulo de Análisis")
    st.write("Aquí pones las funciones de tu segunda aplicación")
