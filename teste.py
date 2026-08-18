import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Dê 3 dicas simples para economizar energia em uma residência.",
)

print(response.text)