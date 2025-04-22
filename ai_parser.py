from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def interpretar_cv(texto_crudo):
    prompt = f"""
Extrae los siguientes datos del siguiente CV:
- Nombre y Apellidos
- Perfil (breve descripción de 3-5 líneas)
- Experiencia Profesional (empresa, localización, rol, fechas, herramientas)
- Formación académica (centro, título, fecha)
- Idiomas
- Habilidades técnicas/directivas (perfil, sistemas operativos, lenguajes, otros)

Texto del CV:
\"\"\"
{texto_crudo}
\"\"\"

Devuelve los datos en este formato JSON:

{{
    "nombre": "",
    "perfil": ["", "", ""],
    "experiencia": [
        {{
            "empresa": "", "localizacion": "", "rol": "", "desde": "", "hasta": "",
            "funcional": "", "herramientas": ""
        }}
    ],
    "formacion": [
        {{"centro": "", "titulo": "", "fecha": ""}}
    ],
    "idiomas": {{
        "ingles": ""
    }},
    "habilidades": {{
        "perfil_principal": "", "perfil_secundario": "", "hardware": "",
        "sistemas_operativos": "", "lenguajes": "", "bbdd": "", "otros": ""
    }}
}}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return eval(response.choices[0].message.content)  # o json.loads si es JSON válido
