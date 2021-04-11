from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/doua")
def joc():
    return render_template("joc.html")
import app
if __name__ == '__main__':
    app.run()