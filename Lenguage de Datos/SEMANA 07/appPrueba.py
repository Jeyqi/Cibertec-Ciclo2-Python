from google import genai

API_KEY = "TU_API_KEY_AQUI"

client = genai.Client(api_key=API_KEY)

try:
    response = client.models.generate_content(
        model = "gemini-3.8-flash",
        contents= "Dame la biografia de Miguel Grau"
    )

    print(response.text)

except Exception as e:
    print(f"Error: {e}")