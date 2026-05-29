
# Prospector Hospitalario Internacional V2

Aplicación web con Streamlit + Gemini API para prospección de hospitales, clínicas y redes sanitarias como posibles sedes de prácticas clínicas para universidades online, híbridas o asincrónicas.

## Novedad V2

Incluye un ranking específico:

**Ranking de intensidad y viabilidad para solicitar prácticas académicas**

Evalúa:

- Acceso a universidades online
- Facilidad de entrada institucional
- Disponibilidad potencial de plazas clínicas
- Costo probable: gratuito, convenio institucional, pago probable o no determinado
- Riesgo regulatorio
- Score de viabilidad de 0 a 100
- Semáforo estratégico
- Intensidad recomendada de acercamiento

## Instalación local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Configuración

Crear archivo:

`.streamlit/secrets.toml`

Con este contenido:

```toml
GEMINI_API_KEY = "TU_API_KEY"
```

## Deploy en Streamlit Cloud

1. Subir este proyecto a GitHub.
2. Conectar el repositorio en Streamlit Community Cloud.
3. Agregar la API Key en Settings > Secrets.
4. Ejecutar la app.
