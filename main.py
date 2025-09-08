from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load env variables from .env if available
load_dotenv()

# Configure API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not set in environment")

genai.configure(api_key=api_key)

INTERNAL_KEY = os.getenv("INTERNAL_API_KEY")
if not INTERNAL_KEY:
    raise ValueError("INTERNAL_API_KEY not set in environment")

app = FastAPI()

# Create model once at startup
model = genai.GenerativeModel("gemini-2.5-flash")


@app.post("/gemini")
async def explain_ai(request: Request):
    data = await request.json()
    input_text = data.get("input")
    language = data.get("language")
    previousContext = data.get("previousContext")

    if not input_text or not language:
        return {"error": "Missing input or language"}

    # Generate response
    response = model.generate_content(
        f'Is this input "{input_text}" about math? '
        f'If so, explain it in "{language}". '
        f'You don\'t need to say yes or no just say the result and if it is not return "បញ្ចូលមិនទាក់ទងនឹងគណិតវិទ្យា។"'
        f' If there is previous context, use it to help explain: "{previousContext}"'
    )

    return {"result": response.text}
