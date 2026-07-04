import streamlit as st

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

# Título y subtítulo principal basado en tu web institucional
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
    st.markdown("#### 📊 BioCore Intelligence App")
    st.caption("Plataforma centralizada para la automatización de datos ecológicos. Permite el procesamiento avanzado de variables y visualización dinámica de indicadores clave para líneas de base e informes de cumplimiento.")
    # El botón abre la app de monitoreo en una pestaña nueva
    st.link_button("Abrir Intelligence App 🚀", "https://biocoreintelligence.streamlit.app/", type="primary")

with col2:
    st.markdown("#### 🔬 DarwinCheck App")
    st.caption("Aplicación web especializada diseñada para auditar, limpiar y corregir bases de datos biológicas complejas. Optimiza los tiempos de control de calidad previos a la entrega de informes técnicos.")
    # El botón abre la app de auditoría en una pestaña nueva
    st.link_button("Abrir DarwinCheck 🧼", "https://darwin-check.streamlit.app/", type="primary")

st.markdown("---")

# Nota informativa elegante al pie de página para los evaluadores del concurso
st.info("💡 **Nota para Capital Pionera:** Esta arquitectura modular permite expandir e integrar de forma económica nuevas herramientas y conectar futuros módulos de **Gemelos Digitales** sin alterar los sistemas en producción.")
