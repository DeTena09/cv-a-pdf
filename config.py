from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PLANTILLA_PATH = "templates/plantilla.docx"
OUTPUT_DIR = "output_docs"