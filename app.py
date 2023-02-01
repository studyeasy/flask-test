from flask import Flask
import semantic_version


app = Flask(__name__)

semantic_version.Version('1.0.0')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"