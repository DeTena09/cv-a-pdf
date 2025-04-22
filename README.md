# Automatización de Conversión de CVs

Este proyecto permite convertir CVs en PDF a documentos `.docx` con formato predefinido, utilizando inteligencia artificial para interpretar el contenido y rellenar una plantilla.

---

## 📁 Estructura del Proyecto

```
cv_automation/
│
├── main.py                         # Script principal
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
├── input_pdfs/
│   └── ejemplo.pdf                 # CVs en PDF
└── output_docs/
    └── ejemplo_generado.docx       # Salida generada
```

---

## ▶️ Cómo usar

1. **Instala dependencias**  
   Ejecuta en tu entorno:

   ```bash
   pip install -r requirements.txt
   ```

2. **Crea un archivo `.env` con tu API key**  
   En la raíz del proyecto, crea un archivo `.env` con el siguiente contenido:

   ```env
   OPENAI_API_KEY=tu_clave_api
   ```

3. **Configura el archivo `config.py`**  
   Ya está preparado para leer automáticamente tu clave desde el `.env`.

4. **Agrega tus CVs**  
   Coloca los archivos PDF dentro de `input_pdfs/`.

5. **Ejecuta el script**  
   Corre el archivo principal:

   ```bash
   python main.py
   ```

---

## 🧠 ¿Cómo funciona?

1. Se extrae texto del CV en PDF.
2. Se analiza el texto con una IA para obtener estructura (nombre, experiencia, estudios...).
3. Se rellena automáticamente un `.docx` con esa información utilizando una plantilla predefinida.

---

## 📌 Requisitos

- Python 3.8 o superior
- Cuenta de OpenAI con clave de API válida

---

## 🛠 En desarrollo

- Soporte para múltiples idiomas
- Procesamiento en lote de múltiples PDFs
- Validación de campos antes de exportar
