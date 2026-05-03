from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "local")

@app.route("/")
def home():
    return f"Hello from production CI/CD demo. corrected one. Version: {VERSION}\n"

@app.route("/health")
def health():
    return "healthy\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
