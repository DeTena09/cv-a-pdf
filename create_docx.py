from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
import os

# Funciones de ayuda
def agregar_titulo(doc, texto):
    p = doc.add_paragraph()
    run = p.add_run(texto.upper())
    run.bold = True
    run.font.size = Pt(16)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(12)

def agregar_subtitulo(doc, texto):
    p = doc.add_paragraph()
    run = p.add_run(texto.upper())
    run.bold = True
    run.underline = True
    run.font.size = Pt(12)
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(8)

def agregar_linea(doc, texto, negrita=False, salto=True):
    p = doc.add_paragraph()
    run = p.add_run(texto)
    run.bold = negrita
    run.font.size = Pt(10)
    if not salto:
        p.paragraph_format.space_after = Pt(0)
    return p

def crear_cv_desde_json(datos, output_path):
    doc = Document()

    # === NOMBRE ===
    agregar_titulo(doc, datos["nombre"])

    # === PROFILE ===
    agregar_subtitulo(doc, "PROFILE:")
    for linea in datos["perfil"]:
        linea = linea.strip()
        if not linea:
            continue
        parrafo = doc.add_paragraph(style="List Bullet")
        parrafo.paragraph_format.left_indent = Inches(0.5)
        parrafo.paragraph_format.first_line_indent = Inches(-0.15)
        if " (" in linea and linea.endswith(")"):
            texto_principal = linea[:linea.rfind(" (")]
            duracion = linea[linea.rfind(" (") + 2 : -1]
            run1 = parrafo.add_run(texto_principal + " (")
            run2 = parrafo.add_run(duracion)
            run2.bold = True
            run3 = parrafo.add_run(")")
        else:
            parrafo.add_run(linea)

    # === EXPERIENCIA PROFESIONAL ===
    agregar_subtitulo(doc, "EXPERIENCIA PROFESIONAL:")
    for exp in datos["experiencia"]:
        table = doc.add_table(rows=1, cols=5)
        table.autofit = True
        table.alignment = WD_ALIGN_PARAGRAPH.LEFT
        cells = table.rows[0].cells
        texto_celdas = [
            exp['empresa'],
            exp['localizacion'] or "",
            exp['rol'],
            f"Desde:\n{exp['desde']}",
            f"Hasta:\n{exp['hasta']}"
        ]
        for i, texto in enumerate(texto_celdas):
            par = cells[i].paragraphs[0]
            run = par.add_run(texto)
            run.bold = True
            run.font.size = Pt(10)
            cells[i].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            par.paragraph_format.space_after = Pt(0)
            par.paragraph_format.space_before = Pt(0)

        p_funcional = doc.add_paragraph()
        p_funcional.paragraph_format.space_before = Pt(10)
        run_funcional = p_funcional.add_run("Experiencia funcional:")
        run_funcional.bold = True

        p_desc = doc.add_paragraph(exp["funcional"])
        p_desc.paragraph_format.line_spacing = 1.3
        p_desc.paragraph_format.space_after = Pt(10)

        p_herr = doc.add_paragraph()
        p_herr.paragraph_format.space_before = Pt(6)
        run_herr = p_herr.add_run("Herramientas:")
        run_herr.bold = True

        p_herr_val = doc.add_paragraph(exp["herramientas"])
        p_herr_val.paragraph_format.line_spacing = 1.3
        p_herr_val.paragraph_format.space_after = Pt(15)

    # === FORMACIÓN ACADÉMICA ===
    agregar_subtitulo(doc, "FORMACIÓN ACADÉMICA:")
    for form in datos["formacion"]:
        agregar_linea(doc, f"{form['titulo']} — {form['centro']} ({form['fecha']})")

    # === CERTIFICADOS ===
    if "certificados" in datos and datos["certificados"]:
        agregar_subtitulo(doc, "CERTIFICACIONES:")
        for cert in datos["certificados"]:
            agregar_linea(doc, f"{cert['nombre']} – {cert['institucion']} ({cert['fecha']})")

    # === IDIOMAS ===
    agregar_subtitulo(doc, "IDIOMAS:")
    for idioma in datos["idiomas"]:
        agregar_linea(doc, f"{idioma['idioma']}: {idioma['nivel']}")

    # === HABILIDADES TÉCNICAS ===
    agregar_subtitulo(doc, "HABILIDADES TÉCNICAS:")
    habilidades = datos["habilidades"]
    agregar_linea(doc, f"Perfil principal: {habilidades['perfil_principal']}")
    agregar_linea(doc, f"Perfil secundario: {habilidades['perfil_secundario']}")
    agregar_linea(doc, f"Herramientas: {habilidades['herramientas']}")
    

    doc.save(output_path)
    return output_path

