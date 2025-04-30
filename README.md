# 🧠 CV Processor 1.0c

Conversor automático de CVs en PDF a Word con formato empresarial. Extrae datos clave usando inteligencia artificial y genera documentos `.docx` listos para entregar, basados en una plantilla profesional (Softtek).

---

## 🚀 Características principales

- 📄 Procesa uno o varios CVs en PDF
- 🤖 Usa OpenAI para extraer datos estructurados (nombre, experiencia, formación, idiomas, etc.)
- 📄 Genera un `.docx` con formato fijo (logo, estilos, tablas, interlineado)
- 🧪 Modo test offline con archivos JSON
- 🖥️ Interfaz local con `tkinter`
- 🔐 Manejo seguro de claves con `.env`

---

## 📦 Requisitos

- Python 3.10+
- Cuenta de OpenAI con clave API

---

## 🔧 Instalación

```bash
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
pip install -r requirements.txt
```

Crea un archivo `.env` en la raíz con tu clave de API:

```env
OPENAI_API_KEY=sk-...
```

---

## 🖥️ Ejecutar la app

```bash
python main.py
```

---

## 📁 Estructura esperada

```
.
├── main.py
├── test.py
├── create_docx.py
├── templates/
│   ├── plantilla.docx
│   └── softtek.png
├── output_docs/
├── .env
├── requirements.txt
└── .github/
    └── workflows/
        └── build-macos.yml
```

---

## ✍️ Créditos

Desarrollado por [DeTena09](https://github.com/DeTena09)  
Versión: `1.0c`
