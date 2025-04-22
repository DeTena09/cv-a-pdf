# Automatización de Conversión de CVs

Este proyecto permite convertir CVs en PDF a documentos `.docx` con formato predefinido, utilizando inteligencia artificial para interpretar el contenido y rellenar una plantilla. Incluye una interfaz gráfica simple para seleccionar múltiples archivos.

---

## 📁 Estructura del Proyecto

```
cv_automation/
│
├── main.py                         # Interfaz gráfica principal
├── pdf_reader.py                   # Extracción de texto desde PDF
├── ai_parser.py                    # Análisis del texto con IA (GPT)
├── docx_writer.py                  # Generación del Word con formato
├── config.py                       # Configuraciones generales y carga del .env
├── requirements.txt                # Librerías necesarias
├── .env                            # Clave API (IGNORADA por Git)
├── .gitignore                      # Archivos ignorados por Git
├── README.md                       # Este archivo
├── templates/
│   └── plantilla.docx              # Plantilla Word
├── input_pdfs/                     # Carpeta temporal de PDFs seleccionados
└── output_docs/                    # Documentos Word generados
```

---

## ▶️ Cómo usar

1. **Instala dependencias**  
   Ejecuta:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configura tu clave de API en un `.env`**  
   En la raíz del proyecto crea un archivo `.env`:

   ```env
   OPENAI_API_KEY=tu_clave_api
   ```

3. **Ejecuta la aplicación con interfaz gráfica**  

   ```bash
   python main.py
   ```

4. **Selecciona uno o más archivos PDF y haz clic en “Procesar”**  
   Los documentos `.docx` se generarán automáticamente y se guardarán en la carpeta `output_docs/`.

---

## 🧠 ¿Cómo funciona?

1. Se extrae el texto del CV desde PDF.
2. Se analiza el contenido con GPT (OpenAI API moderna).
3. Se genera un `.docx` con la estructura deseada.
4. Archivos PDF seleccionados se copian temporalmente a `input_pdfs/` y se eliminan tras el procesamiento.

---

## 📌 Requisitos

- Python 3.8 o superior
- Cuenta de OpenAI con API Key válida

---

## 🛠 En desarrollo

- Soporte multilenguaje
- Procesamiento masivo (batch)
- Vista previa de resultados antes de exportar
