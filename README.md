# Análisis de Sentimientos en Reseñas de Películas

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-009688?style=for-the-badge&logo=fastapi)
![Gradio](https://img.shields.io/badge/Gradio-3.35-FF7C00?style=for-the-badge&logo=gradio)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.2-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

---

## Descripción del Proyecto

Este repositorio contiene una **aplicación web completa** para análisis de sentimientos en reseñas de películas. El sistema utiliza un modelo de Inteligencia Artificial, específicamente una red neuronal *Perceptrón Multicapa* (`MLPClassifier`), para clasificar reseñas como **positivas** o **negativas**.  
Incluye tanto backend como frontend en Python, aplicando un flujo completo de Machine Learning: limpieza de datos, entrenamiento, evaluación y despliegue de una API para consumo externo.

---

## Contexto del Proyecto

> **Proyecto del Segundo Bimestre - Fundamentos de Inteligencia Artificial**  
> **Institución:** Escuela Politécnica Nacional - Escuela de Formación de Tecnólogos  
> **Carrera:** Tecnología Superior en Desarrollo de Software  
> **Asignatura:** Fundamentos de Inteligencia Artificial  
> **Profesor:** Ing. Sergio Granizo MSc.  
> **Período Académico:** 2025-A

---

## Tabla de Contenidos

- [Características Principales](#características-principales)
- [Demostración de la Aplicación](#demostración-de-la-aplicación)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación y Uso](#instalación-y-uso)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Autores](#autores)

---

## Características Principales

- ✅ **Entrenamiento del Modelo:** Detallado en `notebooks/entrenamiento.ipynb`, desde la carga del dataset IMDB hasta el guardado del modelo entrenado.
- ✅ **API Funcional:** Backend robusto con FastAPI, exponiendo el modelo vía endpoint `/predict`.
- ✅ **Frontend Interactivo:** Interfaz gráfica amigable creada con Gradio para predicción en tiempo real.
- ✅ **Métricas de Entrenamiento:** Accuracy, reporte de clasificación y matriz de confusión en el notebook.
- ✅ **Recepción de Nuevos Casos:** El sistema acepta y predice sobre texto nuevo ingresado por el usuario.

---

## Demostración de la Aplicación

La interfaz de usuario (Gradio) permite ingresar una reseña y obtener la predicción del sentimiento:  
> "Positivo" o "Negativo".

> **Nota:** Reemplaza la imagen de abajo por una captura de pantalla o GIF de tu aplicación funcionando.

![Demo](https://i.imgur.com/link-a-tu-imagen.png)

---

## Arquitectura del Sistema

El proyecto sigue una arquitectura cliente-servidor:

- **Modelo de IA:**  
  - `MLPClassifier` de Scikit-learn, entrenado sobre el dataset "IMDB Dataset of 50k Movie Reviews".
  - Transformación de texto a características numéricas vía `TfidfVectorizer`.
- **Backend (API):**  
  - Servidor FastAPI que carga el modelo (`sentiment_model.pkl`) y vectorizador (`vectorizer.pkl`).
  - Endpoint `/predict` para recibir texto y devolver la predicción.
- **Frontend:**  
  - Interfaz Gradio como cliente, enviando texto a la API y mostrando el resultado.

---

## Tecnologías Utilizadas

| Categoría           | Tecnología                                                                                          |
|---------------------|----------------------------------------------------------------------------------------------------|
| Backend             | ![FastAPI](https://img.shields.io/badge/FastAPI-0.95-009688?style=flat-square&logo=fastapi) <br> ![Uvicorn](https://img.shields.io/badge/Uvicorn-22.0-4A9F85?style=flat-square)     |
| Frontend            | ![Gradio](https://img.shields.io/badge/Gradio-3.35-FF7C00?style=flat-square&logo=gradio)           |
| Machine Learning    | ![scikit-learn](https://img.shields.io/badge/scikit--learn-1.2-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) |
| Librerías de Datos  | ![Pandas](https://img.shields.io/badge/Pandas-1.5-150458?style=flat-square&logo=pandas) <br> ![NLTK](https://img.shields.io/badge/NLTK-3.8-3776AB?style=flat-square)             |
| Lenguaje            | ![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python)            |

---

## Instalación y Uso

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

### Prerrequisitos

- Python 3.10+
- Git

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Johh4nn/Proyecto_IA.git
cd Proyecto_IA
```

### 2. Configurar el Entorno Virtual

```bash
# Crear el entorno
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la Aplicación

He preparado un script `main.py` para lanzar backend y frontend de manera concurrente.

```bash
python main.py
```

- El backend (FastAPI) correrá en [http://127.0.0.1:8000](http://127.0.0.1:8000)
- El frontend (Gradio) en [http://127.0.0.1:7860](http://127.0.0.1:7860)

Abre tu navegador y ve a [http://127.0.0.1:7860](http://127.0.0.1:7860) para probar la aplicación.

### 5. Advertencia de Seguridad

⚠️ **Importante:**  
El archivo `kaggle.json` contiene credenciales privadas.  
**Nunca debe ser subido a un repositorio público.**  
Te recomiendo **eliminarlo del historial de git** y **añadirlo a tu `.gitignore`** para prevenir futuras exposiciones.

---

## Estructura del Repositorio

```
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
```

---

## Autores

- **Paulo Cisneros**
- **Eddy Morales**
- **Johan Vargas**
