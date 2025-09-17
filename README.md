## 🌟 About Komplex AI

**Komplex AI Backend** is a high-performance FastAPI service that powers the AI features of the KOMPLEX learning platform. It provides intelligent content generation, educational assistance, and personalized learning support using Google's Gemini 2.5 Flash model.

### Key Capabilities

- 🧠 **Intelligent Tutoring**: AI-powered explanations and problem-solving assistance
- 📚 **Content Generation**: Automatic creation of educational materials and exercises  
- 🎯 **Personalized Learning**: Adaptive responses based on student needs
- 🔒 **Secure Access**: API key authentication and rate limiting
- ⚡ **High Performance**: Optimized for fast response times

---

## ✨ Features

### 🔐 Security & Authentication
- **API Key Authentication**: Secure endpoint protection with `X-API-Key` header
- **Rate Limiting**: Built-in protection against abuse

### 🤖 AI Integration
- **Google Gemini 2.5 Flash**: Latest AI model for educational content
- **Context-Aware Responses**: Understands STEM education context
- **Multi-format Output**: Text, code examples, step-by-step solutions



### 📊 Developer Experience
- **Interactive Docs**: Auto-generated Swagger/OpenAPI documentation
- **Type Safety**: Full Python type hints and validation
- **Docker Support**: Containerized deployment ready

---

## 🏗️ Architecture

```
komplex-ai-backend/
├── main.py                    # FastAPI application entry point
├── requirements.txt           # Python dependencies
├── .env                      # Environment variables
├── Dockerfile                # Docker configuration
├── docker-compose.yml        # Multi-service setup
└── README.md                 # This file
```

---

## 🚀 Quick Start

### Prerequisites

- **Python** 3.8 or higher
- **pip** package manager
- **Google AI Studio API Key** ([Get one here](https://makersuite.google.com/app/apikey))

### Option 1: Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/salxz696969/Komplex_Ai.git
   cd Komplex_Ai
   ```

2. **Create and activate virtual environment**
   ```powershell
   # Windows PowerShell
   python -m venv .venv
   .\.venv\Scripts\activate

   # Linux/macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn python-dotenv google-generativeai
   ```
   
   Or use requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Create .env file
   cp .env.example .env
   ```
   
   Edit `.env` with your configuration:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   INTERNAL_API_KEY=your_secure_internal_api_key
   PORT=8000
   HOST=127.0.0.1
   ```

5. **Start the development server**
   ```bash
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

### Option 2: Docker Deployment

1. **Clone the repository**
   ```bash
   git clone https://github.com/salxz696969/Komplex_Ai.git
   cd Komplex_Ai
   ```

2. **Copy environment example file**
   ```bash
   cp .env.example .env
   ```

3. **Build and start the containers**
   ```bash
   docker-compose up --build
   ```


### 🔧 Environment Configuration

Create a `.env` file with the following variables:

```env
# Required: Google Gemini API Configuration
GEMINI_API_KEY=your_google_gemini_api_key

# Required: Security
INTERNAL_API_KEY=your_secure_random_api_key (same as the one used on the express server)

# Optional: Server Configuration
PORT=8000
HOST=127.0.0.1
DEBUG=true

# Optional: CORS Configuration
ALLOWED_ORIGINS=http://localhost:3000,https://komplex.edu.kh
ALLOWED_METHODS=GET,POST,PUT,DELETE
ALLOWED_HEADERS=*
```

---

## 📡 API Documentation

### Interactive Documentation

Once the server is running, visit:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Core Endpoints

| Endpoint | Method | Description | Authentication |
|----------|--------|-------------|----------------|
| `/gemini` | POST | AI content generation | ✅ API Key Required |


### AI Content Generation

You can generate AI-powered educational content using the `/gemini` endpoint.

#### Using Thunder Client or Postman

1. Open **Thunder Client** (VS Code extension) or **Postman**.
2. Create a new request:
    - Method: `POST`
    - URL: `http://127.0.0.1:8000/gemini`
    - Headers:
      - `X-API-Key: your_internal_api_key`
      - `Content-Type: application/json`
    - Body (JSON):
      ```json
      {
         "input": "Explain the Pythagorean theorem with an example",
         "language": "english",
         "previousContext": ""
      }
      ```
3. Send the request to receive an AI-generated response.

**Response:**
```json
{
  "result": ""
}
```

---

#### Using cURL

```bash
curl -X POST "http://127.0.0.1:8000/gemini" \
  -H "X-API-Key: your_internal_api_key" \
  -H "Content-Type: application/json" \
  -d '{
     "input": "Explain the Pythagorean theorem with an example",
     "language": "english",
     "previousContext": ""
  }'
```



**Response:**
```json
{
  "result": ""
}
```




---
## 🔒 Security Best Practices

### API Key Management

1. **Generate Strong Keys**: Use cryptographically secure random strings
2. **Environment Variables**: Never hardcode keys in source code
3. **Key Rotation**: Regularly rotate API keys
4. **Access Logs**: Monitor API key usage

