from docx import Document

def generar_docx(plantilla_path, datos, output_path):
    doc = Document(plantilla_path)
    for p in doc.paragraphs:
        if "NOMBRE Y APELLIDOS" in p.text:
            p.text = datos["nombre"]
        # Aquí irías añadiendo los demás campos...
    doc.save(output_path)
