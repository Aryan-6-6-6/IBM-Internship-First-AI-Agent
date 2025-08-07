# index.py
from flask import Flask, request, jsonify

# Use this if __init__.py exists in `api` folder
from marine_agent import marine_chat

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "🌊 Marine AI Agent (SDG 14) is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"error": "❌ No query provided."}), 400

    response = marine_chat(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
