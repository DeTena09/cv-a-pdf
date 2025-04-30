from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
IMAGE_PATH = "templates/softteck.png"
OUTPUT_DIR = "output_docs"