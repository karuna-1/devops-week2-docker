import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "development")
    return f"Hello from Docker! Environment: {environment}"

app.run(host="0.0.0.0", port=5000)