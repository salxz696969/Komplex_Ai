from fastapi import FastAPI, Request, Header, HTTPException
from dotenv import load_dotenv
import os
import google.generativeai as genai
from pre_prompt import pre_prompt

# Load env variables
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
async def explain_ai(
    request: Request,
    x_api_key: str = Header(None),  # Expecting a header like:  X-API-Key: <key>
):
    if x_api_key != INTERNAL_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

    data = await request.json()
    input_text = data.get("input")
    language = data.get("language")
    previousContext = data.get("previousContext")

    if not input_text or not language:
        return {"error": "Missing input or language"}

    response = model.generate_content(pre_prompt(input_text, language, previousContext))

    return {"result": response.text}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)