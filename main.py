from fastapi import FastAPI, Request, Header, HTTPException
from dotenv import load_dotenv
import os
import google.generativeai as genai

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

@app.get("/ping")
async def ping():
    return {"message": "pong"}

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

    response = model.generate_content(
        f"""
        You are a helpful science tutor. 
        Your job is to **explain clearly** and **format beautifully**. 
        The input may be about one of these topics:
        - Mathematics
        - Physics
        - Chemistry
        - Biology

        ### Rules:
        1. If the input is about **Math, Physics, Chemistry, or Biology**:
            - Explain in **{language}** only (do not mix with English if {language} is not English).
            - Use a **friendly but professional tone** (like a supportive teacher).
            - Format the response with:
             - **Line breaks** between steps and sections.
             - **Equations** written cleanly (LaTeX style if possible).
             - **Bullet points or numbered steps** when breaking down concepts.
             - **Emojis** where helpful (📘 ➝ topic, 🧮 ➝ math steps, 🧪 ➝ chemistry, ⚛️ ➝ physics, 🧬 ➝ biology).
           - Keep equations and explanations very easy to read, never bury formulas inside text.
           - If there is `previousContext`, use it to improve clarity and continuity.

        2. If the input is **not about these four subjects**, reply in {language} with a short, kind message like:
           "សូមអភ័យទោស 🙏 ខ្ញុំអាចជួយបានតែជាមួយ គណិតវិទ្យា, រូបវិទ្យា, គីមីវិទ្យា និង ជីវវិទ្យា ប៉ុណ្ណោះ។"

        ### Input:
        "{input_text}"

        ### Previous context (if any):
        "{previousContext}"

        Now give the final, well-formatted explanation.
    """
    )

    return {"result": response.text}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)