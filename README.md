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
├── config.py                       # Configuraciones generales
├── requirements.txt                # Librerías necesarias
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

2. **Configura tu API Key**  
   En el archivo `config.py`, coloca tu clave de OpenAI:

   ```python
   OPENAI_API_KEY = "tu_clave_api"
   ```

3. **Agrega tus CVs**  
   Coloca los archivos PDF dentro de `input_pdfs/`.

4. **Ejecuta el script**  
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
