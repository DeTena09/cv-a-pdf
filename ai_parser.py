from openai import OpenAI
from config import OPENAI_API_KEY
import json

client = OpenAI(api_key=OPENAI_API_KEY)



def interpretar_cv(texto_crudo, descripcion):
    prompt = f"""
Estás ayudando a analizar CVs para un proyecto específico.

**Descripción del proyecto:**
{descripcion}

Extrae los siguientes datos del siguiente CV. Responde exclusivamente en **Español neutro y profesional**, como si estuvieras redactando un informe técnico sobre un candidato. Usa tercera persona (no utilices "yo", "he trabajado", "mi experiencia..."). Recuerda que toda la información estará enfocada al proyecto al cual esta siendo seleccionado.
DATOS A EXTRAER:

- Nombre y Apellidos
- Perfil profesional: una lista con formato "Rol – Empresa (duración)", donde la duración sea en años y meses, por ejemplo: "Senior Back-End Engineer – Heytrade (6 meses)". Debe ir ordenado del más reciente al más antiguo.
- Experiencia Profesional (una entrada por cada empresa o proyecto):
 Para cada experiencia profesional, extrae los siguientes datos: nombre de la empresa, localización (ciudad o país si está disponible), puesto o rol desempeñado, fechas de inicio y finalización (usa mes y año), una descripción funcional redactada en tercera persona con un tono técnico y profesional (evitando el uso de la primera persona y el nombre de la persona) y que este desarollado al máximo posible usando tantos parrafos como sea necesario y sin dejarse nada por explicar enfocado en el proyecto al que esta siendo selecionado, y el listado completo de herramientas y tecnologías utilizadas, separadas por comas.
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
        "perfil_principal": "", "perfil_secundario": "", "herramientas": ""
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
