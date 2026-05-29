
import streamlit as st
from google import genai

st.set_page_config(
    page_title="Prospector Hospitalario Internacional",
    page_icon="🏥",
    layout="wide"
)

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

BASE_PROMPT = """
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
- Compatibilidad REAL con estudiantes provenientes de universidades online, híbridas o asincrónicas.
- Viabilidad operativa para solicitar prácticas académicas clínicas.
- Claridad sobre si las prácticas pueden gestionarse de forma gratuita, mediante convenio institucional,
  o si requieren pago por parte de la universidad.

CRITERIO CRÍTICO:
Excluir hospitales que:
- No acepten alumnos de universidades online.
- Requieran únicamente universidades presenciales.
- No admitan estudiantes internacionales.
- Carezcan de estructura docente.
- No tengan evidencia de programas de prácticas, rotaciones, observerships, internships,
  estancias clínicas o vínculos formativos equivalentes.

MÓDULO OBLIGATORIO DE RANKEO DE VIABILIDAD DE PRÁCTICAS:

Además del análisis general, debes crear un ranking visible llamado:

"Ranking de intensidad y viabilidad para solicitar prácticas académicas"

Este ranking debe evaluar cada institución con base en los siguientes criterios:

1. Nivel de acceso para universidades online, híbridas o asincrónicas:
   - Alto: evidencia clara de apertura a estudiantes internacionales, convenios flexibles,
     educación no tradicional o programas observacionales.
   - Medio: no hay prohibición expresa, pero se requiere validación institucional.
   - Bajo: predominan restricciones, convenios cerrados o requisitos presenciales estrictos.

2. Facilidad de entrada institucional:
   - Alta: existe oficina de docencia, relaciones internacionales, formulario público,
     área de prácticas, correo institucional o proceso claro.
   - Media: hay estructura docente, pero el proceso no es completamente transparente.
   - Baja: el acceso depende de contactos internos, convenios previos o procesos poco claros.

3. Disponibilidad potencial de lugares para prácticas clínicas:
   - Alta: hospital grande, alto volumen de pacientes, múltiples especialidades,
     estructura docente consolidada.
   - Media: capacidad razonable, pero limitada por áreas o cupos.
   - Baja: cupos restringidos, baja escala o programas cerrados.

4. Costo o modelo económico probable:
   - Gratuito probable: existe tradición de convenios académicos sin tarifa explícita.
   - Convenio institucional: puede requerir acuerdo marco, pero no necesariamente pago directo.
   - Pago probable: existen indicios de cuotas, fees administrativos, programas internacionales pagados
     o rotaciones privadas.
   - No determinado: no existe información suficiente.

5. Intensidad recomendada de acercamiento:
   Clasifica cada institución como:
   - Prioridad Alta / Atacar primero
   - Prioridad Media / Validar condiciones
   - Prioridad Baja / Mantener como respaldo
   - No recomendable / Excluir o posponer

6. Score final de viabilidad:
   Asigna una calificación de 0 a 100 considerando:
   - Compatibilidad con universidad online: 30%
   - Facilidad de acceso institucional: 25%
   - Disponibilidad de plazas: 25%
   - Costo o gratuidad probable: 10%
   - Riesgo regulatorio: 10%

7. Semáforo visual:
   - Verde: alta viabilidad
   - Amarillo: viable con validación
   - Naranja: riesgo operativo relevante
   - Rojo: baja viabilidad o incompatibilidad

ENTREGABLES:
1. Tabla ejecutiva comparativa.
2. Ranking por ciudad.
3. Ranking por especialidad.
4. Ranking por apertura internacional.
5. Ranking por viabilidad de convenio.
6. Ranking por capacidad de plazas.
7. Ranking de intensidad y viabilidad para solicitar prácticas académicas.
8. Matriz de costo probable: gratuito, convenio institucional, pago probable o no determinado.
9. Lista negra de instituciones incompatibles.
10. Conclusiones ejecutivas.
11. Recomendaciones tácticas.
12. Estrategia sugerida de entrada regional.

FORMATO DEL RANKING DE VIABILIDAD:
Incluye una tabla con estas columnas:
- Posición
- Institución
- Ciudad / País
- Acceso a universidades online
- Facilidad de entrada
- Disponibilidad de plazas
- Costo probable
- Riesgo regulatorio
- Score de viabilidad 0-100
- Semáforo
- Intensidad recomendada de acercamiento
- Justificación breve
"""

with st.sidebar:
    st.title("🏥 Prospectador")

    pais = st.selectbox(
        "País objetivo",
        [
            "España", "Argentina", "Colombia", "Chile", "México",
            "Portugal", "Brasil", "Perú", "Uruguay", "Costa Rica", "Ecuador"
        ]
    )

    ciudad = st.text_input("Ciudad", "Madrid")

    especialidades = st.multiselect(
        "Áreas académicas",
        [
            "Medicina General", "Medicina Interna", "Cirugía", "Odontología",
            "Farmacia", "Enfermería", "Nutrición Clínica", "Fisioterapia",
            "Radiología", "Salud Pública", "Administración Hospitalaria",
            "Investigación Clínica", "Epidemiología", "Medicina Crítica",
            "Urgencias", "Telemedicina", "Gestión Sanitaria"
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

    cantidad = st.slider("Número de instituciones", 5, 30, 10)

    profundidad = st.selectbox(
        "Nivel de análisis",
        ["Ejecutivo", "Detallado", "Muy profundo"]
    )

    prioridad_costo = st.selectbox(
        "Preferencia de modelo económico",
        [
            "Priorizar opciones gratuitas",
            "Aceptar convenios institucionales sin pago directo",
            "Incluir opciones pagadas si son estratégicas",
            "Sin preferencia"
        ]
    )

    extra = st.text_area(
        "Instrucción adicional",
        "Prioriza hospitales con oficinas de relaciones internacionales, docencia médica y programas activos de movilidad clínica."
    )

st.title("Prospector Hospitalario Internacional")
st.caption("Inteligencia estratégica para alianzas hospitalarias, movilidad clínica y convenios académicos.")

if st.button("🔍 Generar Prospección"):
    with st.spinner("Analizando viabilidad hospitalaria y disponibilidad de prácticas..."):

        prompt = f"""
        {BASE_PROMPT}

        Parámetros:
        - País: {pais}
        - Ciudad: {ciudad}
        - Especialidades: {", ".join(especialidades)}
        - Capa estratégica: {capa}
        - Cantidad de instituciones: {cantidad}
        - Profundidad del análisis: {profundidad}
        - Preferencia de modelo económico: {prioridad_costo}

        Instrucción adicional:
        {extra}

        IMPORTANTE:
        Si no existe evidencia clara de compatibilidad con universidades online,
        híbridas o asincrónicas, clasifica el riesgo regulatorio como MEDIO o ALTO.
        No inventes gratuidad: si no hay evidencia, clasifica como "No determinado".
        Diferencia entre prestigio reputacional y facilidad real para obtener prácticas clínicas.
        """

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

