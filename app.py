from flask import Flask

app = Flask(__name__)


@app.route("/check/system/operation")
def home():
    return "All systes operationsl!"


if __name__ == "__main__":
    app.run(debug=True)
