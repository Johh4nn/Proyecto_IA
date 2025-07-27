from flask import Flask, render_template, request
import joblib
import os
import sys

# Ruta al directorio raíz
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, BASE_DIR)

# Importar función de limpieza
from utils.preprocessing import limpiar_texto

# Cargar modelo y vectorizador
MODEL_PATH = os.path.join(BASE_DIR, 'data', 'model', 'sentiment_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'data', 'model', 'vectorizer.pkl')
modelo = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Configuración de Flask
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        texto = request.form.get("texto")
        texto_limpio = limpiar_texto(texto)
        vector = vectorizer.transform([texto_limpio])
        pred = modelo.predict(vector)[0]
        resultado = f"Sentimiento: {pred}"
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
