from flask import render_template
from week1project import app


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")
