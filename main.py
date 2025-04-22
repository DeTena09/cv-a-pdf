from pdf_reader import extraer_texto_pdf
from ai_parser import interpretar_cv
from docx_writer import generar_docx
from config import PLANTILLA_PATH, OUTPUT_DIR

import os

def procesar_cv(pdf_path):
    texto = extraer_texto_pdf(pdf_path)
    datos = interpretar_cv(texto)
    nombre_archivo = os.path.splitext(os.path.basename(pdf_path))[0] + "_generado.docx"
    output_path = os.path.join(OUTPUT_DIR, nombre_archivo)
    generar_docx(PLANTILLA_PATH, datos, output_path)

if __name__ == "__main__":
    procesar_cv("input_pdfs/ejemplo.pdf")
