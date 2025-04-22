import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def interpretar_cv(texto_crudo):
    prompt = f"""[... el mismo prompt largo de antes ...]"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return eval(response.choices[0].message.content)  # o json.loads