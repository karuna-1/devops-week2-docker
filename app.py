import requests
import os
from flask import Flask

app = Flask(__name__)

@app.route("/api")
def call_api():
    response = requests.get("http://api")
    return f"API response: {response.text}"

@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "development")
    return f"Hello from Docker! Environment: {environment}"

app.run(host="0.0.0.0", port=5000)