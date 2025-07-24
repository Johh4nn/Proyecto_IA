import gradio as gr
import joblib
import sys
import os

# Ruta al directorio raíz del proyecto (Proyecto_IA)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)  # usar insert(0) para que tenga prioridad

# Verifica que la ruta esté en sys.path
print("Rutas de búsqueda:")
for p in sys.path:
    print(p)

# Importar función de limpieza
from utils.preprocessing import limpiar_texto

# Rutas absolutas a los modelos
MODEL_PATH = os.path.join(BASE_DIR, 'data', 'model', 'sentiment_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'data', 'model','vectorizer.pkl')

# Cargar modelo y vectorizador
modelo = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Función de análisis
def analizar_sentimiento(texto):
    texto_limpio = limpiar_texto(texto)
    vector = vectorizer.transform([texto_limpio])
    pred = modelo.predict(vector)[0]
    return f"Sentimiento: {pred}"

# Interfaz Gradio
app = gr.Interface(
    fn=analizar_sentimiento,
    inputs="text",
    outputs="text",
    title="Analizador de Sentimientos",
    description="Escribe una frase y descubre si el sentimiento es positivo, negativo o neutro.",
    theme=gr.themes.Soft()
)

app.launch()
