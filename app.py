from flask import Flask, jsonify, request
from core.brain import Brain

app = Flask(__name__)
brain = Brain()

@app.get("/")
def home():
    return jsonify({
        "name": "Kinex IA",
        "version": "0.1.0",
        "status": "online",
        "message": "Kinex IA core is running."
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"})

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "message is required"}), 400
    return jsonify(brain.chat(message))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
