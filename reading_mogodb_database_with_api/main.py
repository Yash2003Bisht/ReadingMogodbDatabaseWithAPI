from flask import Flask, render_template, json
import requests

app = Flask(__name__)
API_KEY = "f650fd2ab6msha4df27f0b9da9f5"

@app.route("/")
def index():
    try:
        data = requests.get(f"http://127.0.0.1:5555//mongodb-api/userapi={API_KEY}")
    except Exception:
        return "Api server not found"
    return render_template("index.html", data = json.loads(data.text))

if __name__ == "__main__":
    app.run(debug=True)
