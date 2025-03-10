import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

client = genai.Client(api_key = api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents = "hi how are u my dear sexy gemini"
)
print(response.text)