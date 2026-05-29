
import streamlit as st
from google import genai
import pandas as pd

st.set_page_config(
    page_title="Prospector Hospitalario Internacional",
    page_icon="🏥",
    layout="wide"
)

# =========================
# CONFIG GEMINI
# =========================
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# =========================
# PROMPT BASE
# =========================
BASE_PROMPT = '''
Actúa como un consultor senior especializado en alianzas hospitalarias internacionales,
educación médica global, movilidad clínica y vinculación académico-sanitaria para universidades internacionales
con programas online, híbridos y asincrónicos.

Tu misión es desarrollar una prospección estratégica avanzada de hospitales, clínicas,
sanatorios, centros médicos, hospitales universitarios, hospitales generales,
hospitales regionales, hospitales de alta especialidad, institutos nacionales de salud
y redes hospitalarias públicas o privadas que puedan funcionar como sedes receptoras
de prácticas clínicas, rotaciones, estancias observacionales, externados,
internships médicos y programas de formación práctica para estudiantes internacionales.

OBJETIVO CENTRAL:
Identificar instituciones médicas con:
- Alto prestigio clínico.
- Capacidad docente.
- Infraestructura hospitalaria consolidada.
- Potencial real de colaboración internacional.
- Compatibilidad REAL con estudiantes provenientes de universidades online,
  híbridas o asincrónicas.

CRITERIO CRÍTICO:
Excluir hospitales que:
- No acepten alumnos de universidades online.
- Requieran únicamente universidades presenciales.
- No admitan estudiantes internacionales.
- Carezcan de estructura docente.

ENTREGABLES:
1. Tabla ejecutiva comparativa.
2. Ranking por ciudad.
3. Ranking por especialidad.
4. Ranking por apertura internacional.
5. Ranking por viabilidad de convenio.
6. Ranking por capacidad de plazas.
7. Lista negra de instituciones incompatibles.
8. Conclusiones ejecutivas.
9. Recomendaciones tácticas.
10. Estrategia sugerida de entrada regional.
'''

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.title("🏥 Prospectador")

    pais = st.selectbox(
        "País objetivo",
        [
            "España",
            "Argentina",
            "Colombia",
            "Chile",
            "México",
            "Portugal",
            "Brasil",
            "Perú",
            "Uruguay",
            "Costa Rica",
            "Ecuador"
        ]
    )

    ciudad = st.text_input("Ciudad", "Madrid")

    especialidades = st.multiselect(
        "Áreas académicas",
        [
            "Medicina General",
            "Medicina Interna",
            "Cirugía",
            "Odontología",
            "Farmacia",
            "Enfermería",
            "Nutrición Clínica",
            "Fisioterapia",
            "Radiología",
            "Salud Pública",
            "Administración Hospitalaria",
            "Investigación Clínica",
            "Epidemiología",
            "Medicina Crítica",
            "Urgencias",
            "Telemedicina",
            "Gestión Sanitaria"
        ],
        default=["Medicina General", "Enfermería"]
    )

    capa = st.selectbox(
        "Capa estratégica",
        [
            "Todas",
            "Capa 1 — Hospitales de élite internacional",
            "Capa 2 — Hospitales universitarios",
            "Capa 3 — Redes privadas",
            "Capa 4 — Instituciones regionales",
            "Capa 5 — Expansión masiva"
        ]
    )

    cantidad = st.slider(
        "Número de instituciones",
        min_value=5,
        max_value=30,
        value=10
    )

    profundidad = st.selectbox(
        "Nivel de análisis",
        ["Ejecutivo", "Detallado", "Muy profundo"]
    )

    extra = st.text_area(
        "Instrucción adicional",
        "Prioriza hospitales con oficinas de relaciones internacionales y programas activos de movilidad clínica."
    )

# =========================
# HEADER
# =========================
st.title("Prospector Hospitalario Internacional")
st.caption(
    "Inteligencia estratégica para alianzas hospitalarias, movilidad clínica y convenios académicos."
)

# =========================
# BOTÓN
# =========================
if st.button("🔍 Generar Prospección"):
    with st.spinner("Analizando ecosistema hospitalario internacional..."):

        prompt = f'''
        {BASE_PROMPT}

        Parámetros:
        - País: {pais}
        - Ciudad: {ciudad}
        - Especialidades: {", ".join(especialidades)}
        - Capa estratégica: {capa}
        - Cantidad de instituciones: {cantidad}
        - Profundidad del análisis: {profundidad}

        Instrucción adicional:
        {extra}

        IMPORTANTE:
        Si no existe evidencia clara de compatibilidad con universidades online
        o asincrónicas, clasifica el riesgo regulatorio como MEDIO o ALTO.
        '''

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        resultado = response.text

        st.success("Prospección completada.")
        st.markdown(resultado)

        st.download_button(
            label="⬇ Descargar reporte",
            data=resultado,
            file_name=f"prospecto_{pais}_{ciudad}.md",
            mime="text/markdown"
        )
