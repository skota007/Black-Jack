from flask import Flask, render_template
import app

app = Flask(__name__)
server = flask.Flask(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/doua")
def joc():
    return render_template("joc.html")

if __name__ == '__main__':
    app.run()