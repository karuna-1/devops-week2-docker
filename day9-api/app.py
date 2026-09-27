from flask import Flask

app = Flask(__name__)

@app.route("/api")
def api():
    return {"message": "Hello from API v2"}

app.run(host="0.0.0.0", port=5001)