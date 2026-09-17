# 🐍 Taller 3 — Python & Machine Learning

**Autor:** Angelo Martínez Díaz
**Programa:** Análisis y Desarrollo de Software (ADSO) — SENA, regional Antioquia
**Ficha:** 3406204

Proyecto de práctica que cubre un flujo completo de Machine Learning: carga de datos, y el desarrollo y despliegue de **3 modelos** con distintas técnicas (clasificación, regresión y visión artificial).

---

## 📁 Estructura del proyecto

```
taller3_pyml/
├── Carga_datos/                          # Notebooks: cargar datos desde distintas fuentes
│   ├── 1.csv_carga_datos.ipynb
│   ├── 2.excel_carga_datos.ipynb
│   ├── 3.api_carga_datos.ipynb
│   ├── 4.webscraping_carga_datos.ipynb
│   ├── dataset_ventas.csv
│   └── dataset_ventas.xlsx
│
├── Modelos_ML/
│   ├── RandomForest/                     # Modelo 1: Clasificación (diagnóstico clínico)
│   │   ├── 1.Crear_dataset.py
│   │   ├── 2.Entrenar_modelo.py
│   │   ├── 3.Predecir_enfermedad.py      # App Streamlit
│   │   ├── data/
│   │   └── models/
│   │
│   ├── RegresionLineal/                  # Modelo 2: Regresión (precio de vivienda)
│   │   ├── back/                         # API en FastAPI
│   │   │   ├── main.py
│   │   │   ├── train.py
│   │   │   └── Dockerfile
│   │   └── front/                        # Cliente web en Django
│   │       ├── app_predicc/
│   │       ├── config/
│   │       └── Dockerfile
│   │
│   └── VisionArtificial/                 # Modelo 3: Visión artificial (detección de rostros)
│       ├── index.ipynb
│       ├── haarcascade_frontalface_default.xml
│       └── py_img-main/                  # Clon personalizado del repo py_img (Flask + OpenCV)
│           ├── api/index.py
│           ├── public/
│           └── vercel.json
│
└── README.md
```

---

## 🚀 Instalación general

Requiere **Python 3.10+**.

```bash
python -m venv venv

# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

Cada modelo tiene su propio `requirements.txt`; instálalo desde la carpeta correspondiente antes de ejecutarlo.

---

## 🤖 Modelo 1 — Random Forest: Diagnóstico clínico

Clasificador que predice 5 posibles diagnósticos (`infarto`, `neumonia`, `gripe`, `ansiedad`, `gastroenteritis`) a partir de 34 variables clínicas (signos vitales, factores de riesgo y síntomas).

**Stack:** Python, scikit-learn, Pandas, Streamlit, Plotly.

```bash
cd Modelos_ML/RandomForest
python 1.Crear_dataset.py        # genera el dataset sintético
python 2.Entrenar_modelo.py      # entrena y guarda el modelo (.pkl)
streamlit run 3.Predecir_enfermedad.py
```

La app se abre en `http://localhost:8501`. Devuelve el diagnóstico más probable, su nivel de confianza y una recomendación clínica asociada.

> Ejecución local. *(Si además lo desplegaste en Streamlit Community Cloud u otro servicio, agrega aquí el enlace.)*

---

## 🏠 Modelo 2 — Regresión Lineal: Predicción de precio de vivienda

Predice el precio de una vivienda a partir de su superficie en m², usando un modelo de regresión lineal.

**Backend (FastAPI):** expone el endpoint `POST /predict`, recibe `area_m2` y devuelve el precio estimado.
**Frontend (Django):** formulario web que consume la API y muestra el resultado formateado en pesos colombianos.

**Stack:** FastAPI, scikit-learn, joblib · Django, Gunicorn · Docker.

🔗 **Desplegado en Railway:**

| Servicio | URL | Estado |
|---|---|---|
| Frontend | https://blo-front.up.railway.app | 🟢 Online |
| Backend (API) | https://blo-back.up.railway.app | 🟢 Online |

---

## 👁️ Modelo 3 — Visión Artificial: Detección de rostros en tiempo real

Clon personalizado del repositorio **py_img** suministrado por el docente. Detecta rostros en imágenes subidas por el usuario o en video en vivo desde la cámara web, usando OpenCV (Haar Cascade) sobre un backend Flask.

**Personalización realizada sobre la plantilla original:**
- Rebranding completo a **"Anglo Vision Lab"** (título, meta tags, favicon, autor).
- Interfaz rediseñada estilo "cartoon" con selector Subir imagen / Usar cámara.
- Textos y mensajes de la interfaz traducidos y adaptados al español.

**Stack:** Python, Flask, OpenCV (`opencv-python-headless`), HTML/CSS/JS, Bootstrap 5.

🔗 **Desplegado en Vercel:** https://taller-3-pyes.vercel.app

---

## 📓 Carga de datos (notebooks)

Ejercicios de carga y preprocesamiento de datos desde distintas fuentes (CSV, Excel, API REST y web scraping), incluyendo limpieza, codificación de variables, normalización y balanceo de clases con SMOTE.

```bash
cd Carga_datos
jupyter notebook
```

---

## 🔗 Enlaces del proyecto

- **Repositorio GitHub:** https://github.com/angelots31/taller_3_pyes

---

## 🔧 Solución de problemas

- **`imbalanced-learn` no encontrado** → `pip install -r requirements.txt` o `pip install imbalanced-learn`.
- **Warning de versión al cargar un `.pkl`** → el modelo fue entrenado con otra versión de scikit-learn; sigue funcionando igual.
- **No conecta con la API (Regresión Lineal)** → verifica que la variable de entorno `API_URL` apunte al backend correcto en Railway.
- **Error al leer el Excel** → `pip install openpyxl`.