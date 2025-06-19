from flask import Flask
import os

app = Flask(__name__)
backend_id = os.environ.get("BACKEND_ID", "unknown")

@app.route("/")
def index():
    return f"Hola desde backend {backend_id}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
