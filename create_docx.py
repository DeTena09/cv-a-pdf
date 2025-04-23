from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH


def crear_cv_desde_json(datos, output_path):
    doc = Document()

    def agregar_titulo(texto):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(texto.upper())
        run.bold = True
        run.font.size = Pt(16)

    def agregar_subtitulo(texto):
        p = doc.add_paragraph()
        run = p.add_run(texto)
        run.bold = True
        run.font.size = Pt(12)

    def agregar_linea(texto, negrita=False, salto=True):
        p = doc.add_paragraph()
        run = p.add_run(texto)
        run.bold = negrita
        run.font.size = Pt(10)
        if not salto:
            p.paragraph_format.space_after = Pt(0)

    # === NOMBRE ===
    agregar_titulo(datos["nombre"])

    # === PROFILE ===
    agregar_subtitulo("PROFILE:")
    for linea in datos["perfil"]:
        agregar_linea(f"• {linea}")

    # === EXPERIENCIA PROFESIONAL ===
    agregar_subtitulo("\nEXPERIENCIA PROFESIONAL:")
    for exp in datos["experiencia"]:
        agregar_linea(f"{exp['empresa']} — {exp['rol']}", negrita=True)
        agregar_linea(f"Desde {exp['desde']} — Hasta: {exp['hasta']}")
        if exp["localizacion"]:
            agregar_linea(f"Ubicación: {exp['localizacion']}")
        agregar_linea("Experiencia funcional:", negrita=True)
        agregar_linea(exp["funcional"])
        agregar_linea("Herramientas:", negrita=True)
        agregar_linea(exp["herramientas"])
        agregar_linea("")  # espacio entre experiencias

    # === FORMACIÓN ACADÉMICA ===
    agregar_subtitulo("\nFORMACIÓN ACADÉMICA:")
    for form in datos["formacion"]:
        agregar_linea(f"{form['titulo']} — {form['centro']} ({form['fecha']})")

    # === CERTIFICADOS ===
    if "certificados" in datos and datos["certificados"]:
        agregar_subtitulo("\nCERTIFICACIONES:")
        for cert in datos["certificados"]:
            agregar_linea(f"{cert['nombre']} – {cert['institucion']} ({cert['fecha']})")

    # === IDIOMAS ===
    agregar_subtitulo("\nIDIOMAS:")
    for idioma in datos["idiomas"]:
        idioma_nombre = idioma["idioma"]
        nivel = idioma["nivel"]
        agregar_linea(f"{idioma_nombre}: {nivel}")

    # === HABILIDADES TÉCNICAS ===
    agregar_subtitulo("\nHABILIDADES TÉCNICAS:")
    habilidades = datos["habilidades"]
    agregar_linea(f"Perfil principal: {habilidades['perfil_principal']}")
    agregar_linea(f"Perfil secundario: {habilidades['perfil_secundario']}")
    agregar_linea(f"Herramientas: {habilidades['herramientas']}")

    doc.save(output_path)
    print(f"CV generado correctamente en: {output_path}")
