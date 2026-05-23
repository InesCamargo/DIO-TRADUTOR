import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DIO_API_KEY"),
    base_url="https://novo-tradutor-dio.openai.azure.com/openai/deployments"
)

def traduzir(texto, idioma_destino="pt"):
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",  # nome do deployment da DIO
        messages=[
            {"role": "system", "content": f"Traduza o texto para {idioma_destino}."},
            {"role": "user", "content": texto}
        ]
    )
    return resposta.choices[0].message["content"]

print(traduzir("Hello, how are you?", "pt"))
