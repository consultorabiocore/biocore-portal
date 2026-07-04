import streamlit as st
import os

# Configuración de la página (Pestaña del navegador)
st.set_page_config(
    page_title="BioCore - Inteligencia Ecológica", 
    page_icon="🌱",
    layout="centered"
)

# Estilo personalizado para botones limpios y alineados
st.markdown("""
    <style>
    div.stButton > button:first-child {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Imagen del Título Principal
if os.path.exists("Titulo.jpg"):
    st.image("Titulo.jpg", use_container_width=True)
else:
    # Si por alguna razón no se encuentra, muestra el título en texto
    st.title("🌱 BioCore")

st.subheader("Diagnóstico ecológico y automatización de datos para el SEIA")

st.markdown("""
Transformamos datos crudos en inteligencia ecológica y soluciones interactivas en Streamlit para consultoría ambiental de alta precisión. 

*Esta plataforma centralizada actúa como nuestro Hub principal de soluciones tecnológicas para la postulación a **Capital Pionera**.*
""")

st.markdown("---")
st.markdown("### 🛠️ Nuestras Soluciones Desplegadas")
st.write("Utiliza los módulos interactivos a continuación para auditar o procesar tus datos ambientales:")

# Crear dos columnas simétricas para presentar las dos apps
col1, col2 = st.columns(2)

with col1:
    # 2. Logo de la App 1 (BioCore Intelligence)
    if os.path.exists("logo_biocore(1).png"):
        st.image("logo_biocore(1).png", use_container_width=True)
    
    st.markdown("#### 📊 BioCore Intelligence App")
    st.caption("Plataforma centralizada para la automatización de datos ecológicos. Permite el procesamiento avanzado de variables y visualización dinámica de indicadores clave para líneas de base e informes de cumplimiento.")
    st.link_button("Abrir Intelligence App 🚀", "https://biocoreintelligence.streamlit.app/", type="primary")

with col2:
    # 3. Logo de la App 2 (DarwinCheck)
    if os.path.exists("logo(1).png"):
        st.image("logo(1).png", use_container_width=True)
        
    st.markdown("#### 🔬 DarwinCheck App")
    st.caption("Aplicación web especializada diseñada para auditar, limpiar y corregir bases de datos biológicas complejas. Optimiza los tiempos de control de calidad previos a la entrega de informes técnicos.")
    st.link_button("Abrir DarwinCheck 🧼", "https://darwin-check.streamlit.app/", type="primary")

st.markdown("---")

# Nota informativa elegante al pie de página para los evaluadores del concurso
st.info("💡 **Nota para Capital Pionera:** Esta arquitectura modular permite expandir e integrar de forma económica nuevas herramientas y conectar futuros módulos de **Gemelos Digitales** sin alterar los sistemas en producción.")
