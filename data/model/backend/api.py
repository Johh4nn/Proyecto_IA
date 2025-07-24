from flask import Flask, request, jsonify
import joblib
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from utils.preprocessing import limpiar_texto
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Construir la ruta absoluta al modelo
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'sentiment_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'model', 'vectorizer.pkl')

# Cargar modelo y vectorizer
modelo = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    texto = limpiar_texto(data["text"])
    vector = vectorizer.transform([texto])
    prediction = modelo.predict(vector)[0]
    return jsonify({"sentiment": prediction})

@app.route("/", methods=["GET"])
def home():
    return "Servidor de análisis de sentimientos activo"

if __name__ == "__main__":
    app.run(debug=True)
