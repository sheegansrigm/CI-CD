from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello from AI Agent Demo!"})

@app.route("/health")
def health():
    return jsonify({"status": "okokok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
