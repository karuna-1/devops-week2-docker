from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    api_url = os.getenv("API_URL", "http://day9-api-container:5001")
    response = requests.get(f"{api_url}/api")
    return f"<h1>Web App</h1><p>{response.json()['message']}</p>"

app.run(host="0.0.0.0", port=5002)