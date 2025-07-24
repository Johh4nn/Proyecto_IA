# utils/preprocessing.py

import re
import nltk
import string
import pandas as pd
from nltk.corpus import stopwords

# Descargar recursos y mostrar rutas
nltk.download('punkt', quiet=False)
nltk.download('stopwords', quiet=False)
print(nltk.data.path)

# Lista de stopwords en inglés
stop_words = set(stopwords.words('english'))

def limpiar_texto(texto):
    """
    Limpia un texto: minúsculas, elimina puntuación, stopwords y números.
    """
    # Minúsculas
    texto = texto.lower()
    
    # Eliminar HTML tags (por si acaso)
    texto = re.sub(r'<.*?>', '', texto)

    # Eliminar números
    texto = re.sub(r'\d+', '', texto)

    # Eliminar puntuación
    texto = texto.translate(str.maketrans('', '', string.punctuation))

    # Tokenizar (dividir en palabras)
    tokens = nltk.word_tokenize(texto)

    # Eliminar stopwords
    tokens_limpios = [word for word in tokens if word not in stop_words]

    # Unir tokens de nuevo en texto
    texto_limpio = ' '.join(tokens_limpios)

    return texto_limpio


def limpiar_dataset(df, texto_col='review', etiqueta_col='sentiment'):
    """
    Aplica limpieza a todo el dataset.
    """
    df = df[[texto_col, etiqueta_col]].copy()
    df.dropna(inplace=True)
    df[texto_col] = df[texto_col].apply(limpiar_texto)
    return df
