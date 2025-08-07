# agent.py
import os
import fitz  # PyMuPDF
from docx import Document
from openai import OpenAI

# === CONFIGURATION ===
# GITHUB_AI_TOKEN = os.environ.get("GITHUB_AI_TOKEN", "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")
GITHUB_AI_TOKEN = os.environ.get("GITHUB_AI_TOKEN", "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")
OPENAI_BASE_URL = "https://models.github.ai/inference"
OPENAI_MODEL = "openai/gpt-4.1"

client = OpenAI(
    base_url=OPENAI_BASE_URL,
    api_key=GITHUB_AI_TOKEN
)

SYSTEM_PROMPT = """
You are a helpful, warm, and focused Under Water life assistant and life below water assistant. You ONLY assist with:
- Understanding About under water life.
- Tell about their types, their species, and their history.
- Suggesting any type of advice related to marine or water life (when user asks).
- Discussion related to marine life or life below water.
- Suggesting any type of advice related to the marine or water pets of any user (when user asks).

❌ If a user asks something unrelated (like geography, programming, etc), politely redirect them back to these marine tasks.
"""

def get_response(query: str) -> str:
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": query}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ API Error: {e}"

# Optional: File reader (if you want to support .pdf/.docx/.txt inputs)
def extract_text(file_path: str) -> str:
    try:
        if file_path.endswith(".pdf"):
            doc = fitz.open(file_path)
            return "\n".join(page.get_text() for page in doc)
        elif file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            return "\n".join(p.text for p in doc.paragraphs)
    except Exception as e:
        print(f"❌ File parsing failed: {e}")
    return None

def marine_chat(query: str) -> str:
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": query}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ API Error: {e}"
