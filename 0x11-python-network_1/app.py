from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/status_401")
def status_401():
    return "", 401

@app.route("/status_500")
def status_500():
    return "", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
