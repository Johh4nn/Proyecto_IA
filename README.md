Análisis de Sentimientos en Reseñas de Películas


![alt text](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![alt text](https://img.shields.io/badge/FastAPI-0.95-009688?style=for-the-badge&logo=fastapi)
![alt text](https://img.shields.io/badge/Gradio-3.35-FF7C00?style=for-the-badge&logo=gradio)
![alt text](https://img.shields.io/badge/scikit--learn-1.2-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)



Descripción del Proyecto
Este repositorio contiene una aplicación web completa diseñada para realizar análisis de sentimientos. El sistema utiliza un modelo de Inteligencia Artificial, específicamente una red neuronal de tipo Perceptrón Multicapa (MLPClassifier), para clasificar reseñas de películas como positivas o negativas.
El proyecto cumple con los objetivos de desarrollar una solución funcional (backend y frontend) en Python, aplicando un flujo de trabajo de Machine Learning que incluye limpieza de datos, entrenamiento del modelo, evaluación de métricas y la implementación de una API para su consumo.


Contexto del Proyecto

Este trabajo fue realizado como parte del Proyecto del Segundo Bimestre para la asignatura de Fundamentos de Inteligencia Artificial.
Institución: Escuela Politécnica Nacional - Escuela de Formación de Tecnólogos
Carrera: Tecnología Superior en Desarrollo de Software
Asignatura: Fundamentos de Inteligencia Artificial
Profesor: Ing. Sergio Granizo MSc.
Período Académico: 2025-A


Tabla de Contenidos
Características Principales
Demostración de la Aplicación
Arquitectura del Sistema
Tecnologías Utilizadas
Instalación y Uso
Estructura del Repositorio
Autores

Características Principales
✅ Entrenamiento del Modelo: El notebook entrenamiento.ipynb detalla el proceso completo de entrenamiento, desde la carga del dataset IMDB hasta el guardado del modelo.
✅ API Funcional: Un backend robusto construido con FastAPI que expone el modelo a través de un endpoint /predict para su consumo.
✅ Frontend Interactivo: Una interfaz gráfica amigable creada con Gradio que permite a los usuarios introducir texto y recibir la clasificación del sentimiento en tiempo real.
✅ Métricas de Entrenamiento: El notebook muestra métricas clave como accuracy, reporte de clasificación y matriz de confusión para evaluar el rendimiento del modelo.
✅ Recepción de Nuevos Casos: El sistema está diseñado para recibir y procesar texto nuevo a través de la interfaz gráfica.

Demostración de la Aplicación
La interfaz de usuario, creada con Gradio, permite una interacción simple y directa. El usuario introduce una reseña de película en el campo de texto y la aplicación devuelve la predicción del sentimiento ("Positivo" o "Negativo").
(Nota Importante: Reemplaza esta imagen con una captura de pantalla o un GIF de tu aplicación funcionando. Este es un elemento visual clave.)
![alt text](https'://i.imgur.com/link-a-tu-imagen.png')


Arquitectura del Sistema
El proyecto sigue una arquitectura cliente-servidor:
Modelo de IA: Un MLPClassifier de Scikit-learn, entrenado sobre el dataset "IMDB Dataset of 50k Movie Reviews". El texto se convierte en características numéricas usando TfidfVectorizer.
Backend (API): Un servidor web construido con FastAPI que carga el modelo (sentiment_model.pkl) y el vectorizador (vectorizer.pkl). Expone un endpoint /predict que recibe texto, lo procesa y devuelve la predicción.
Frontend: Una interfaz de usuario interactiva creada con Gradio. Esta actúa como cliente, enviando el texto del usuario a la API del backend y mostrando la respuesta.

Tecnologías Utilizadas
Categoría	Tecnología
Backend	
![alt text](https://img.shields.io/badge/FastAPI-0.95-009688?style=flat-square&logo=fastapi)
y
![alt text](https://img.shields.io/badge/Uvicorn-22.0-4A9F85?style=flat-square)
Frontend	
![alt text](https://img.shields.io/badge/Gradio-3.35-FF7C00?style=flat-square&logo=gradio)
Machine Learning	
![alt text](https://img.shields.io/badge/scikit--learn-1.2-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
Librerías de Datos	
![alt text](https://img.shields.io/badge/Pandas-1.5-150458?style=flat-square&logo=pandas)
y
![alt text](https://img.shields.io/badge/NLTK-3.8-3776AB?style=flat-square)
Lenguaje	
![alt text](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python)


Instalación y Uso
Sigue estos pasos para ejecutar el proyecto en tu máquina local.
Prerrequisitos
Python 3.10+
Git
1. Clonar el Repositorio
Generated bash
git clone https://github.com/Johh4nn/Proyecto_IA.git
cd Proyecto_IA
Use code with caution.
Bash
2. Configurar el Entorno Virtual
Generated bash
# Crear el entorno
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate
Use code with caution.
Bash
3. Instalar Dependencias
Todas las librerías necesarias están listadas en requirements.txt.
Generated bash
pip install -r requirements.txt
Use code with caution.
Bash
4. Ejecutar la Aplicación
He preparado un script main.py que lanza tanto el backend como el frontend de manera concurrente para facilitar el uso.
Generated bash
python main.py
Use code with caution.
Bash
El backend (FastAPI) se iniciará en http://127.0.0.1:8000.
El frontend (Gradio) se iniciará en http://127.0.0.1:7860.
Para usar la aplicación, abre tu navegador y ve a http://127.0.0.1:7860.


5. Advertencia de Seguridad
⚠️ Importante: El archivo kaggle.json contiene credenciales privadas. Nunca debe ser subido a un repositorio público. Te recomiendo eliminarlo del historial de git y añadirlo a tu archivo .gitignore para prevenir futuras exposiciones.


Estructura del Repositorio


Generated code
Proyecto_IA/
├── .gradio/
├── .venv/
├── data/
│   ├── model/
│   │   └── backend/
│   │       ├── api.py              # Lógica del servidor FastAPI
│   │       ├── sentiment_model.pkl # Modelo de ML entrenado
│   │       └── vectorizer.pkl      # Vectorizador de texto guardado
│   ├── processed/
│   │   ├── emotions_train_limpio.csv
│   │   └── imdb_limpio.csv         # Dataset IMDB procesado
│   └── raw/
│       └── IMDB Dataset.csv        # Dataset original
├── frontend/
│   └── app.py                      # Lógica de la interfaz con Gradio
├── notebooks/
│   └── entrenamiento.ipynb         # Proceso completo de entrenamiento
├── utils/
│   └── preprocessing.py            # Funciones de limpieza de texto
├── .gitignore
├── kaggle.json                     # (Eliminar y añadir a .gitignore)
├── main.py                         # Script principal para lanzar la app
├── README.md
└── requirements.txt                # Dependencias del proyecto
Use code with caution.


Autores
Paulo Cisneros
Eddy Morales
Johan Vargas
