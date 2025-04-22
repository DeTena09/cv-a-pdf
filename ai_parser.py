from openai import OpenAI
from config import OPENAI_API_KEY
import json

client = OpenAI(api_key=OPENAI_API_KEY)



def interpretar_cv(texto_crudo):
    prompt = f"""
Extrae los siguientes datos del CV que te muestro a continuación. La respuesta debe estar completamente en **español**, sin usar palabras en inglés, con excepcion de titulos, tecnologias etc.

DATOS A EXTRAER:

- Nombre y Apellidos
- Perfil profesional: una lista con formato "Rol – Empresa (duración)", donde la duración sea en años y meses, por ejemplo: "Senior Back-End Engineer – Heytrade (6 meses)". Debe ir ordenado del más reciente al más antiguo.
- Experiencia Profesional (una entrada por cada empresa o proyecto):
  - Empresa, localización (ciudad o país si está disponible), rol, fecha de inicio y fin (puedes usar mes y año), descripción funcional y herramientas/tecnologías utilizadas
- Formación académica (centro, título, fecha de inicio y fin o solo año si no se especifica más)
- Idiomas (lista con idioma y nivel, por ejemplo: "Español: nativo", "Inglés: C1")
- Habilidades técnicas y directivas:
  - Perfil principal, perfil secundario, hardware, sistemas operativos, lenguajes de programación, bases de datos, otras herramientas

Texto del CV:
\"\"\" 
{texto_crudo}
\"\"\"

Devuelve los datos en este formato JSON (con todos los textos completamente en español si algun dato se te pasa en ingles traducelo con excepcion de titulos, tecnologias etc):

{{
    "nombre": "",
    "perfil": [
        "Rol – Empresa (duración)",
        "..."
    ],
    "experiencia": [
        {{
            "empresa": "", "localizacion": "", "rol": "", "desde": "", "hasta": "",
            "funcional": "", "herramientas": ""
        }}
    ],
    "formacion": [
        {{
            "centro": "", "titulo": "", "fecha": ""
        }}
    ],
    "idiomas": [
        {{
            "idioma": "", "nivel": ""
        }}
    ],
    "habilidades": {{
        "perfil_principal": "", "perfil_secundario": "", "hardware": "",
        "sistemas_operativos": "", "lenguajes": "", "bbdd": "", "otros": ""
    }}
}}
"""




    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    respuesta = response.choices[0].message.content.strip()
    inicio = respuesta.find("{")
    fin = respuesta.rfind("}") + 1
    bloque_json = respuesta[inicio:fin]
    return json.loads(bloque_json)
