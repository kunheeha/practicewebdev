from flask import render_template, request
from week1project import app


@app.route('/', methods=['POST', 'GET'])
def index():
    myshapes = ['triangle', 'rectangle', 'hexagon']
    if request.method == 'POST':
        shape = request.form["shapeInput"]
        tocheck = shape.lower()
        toreturn = "no"
        for shape in myshapes:
            if tocheck == shape:
                toreturn = shape
                break

        return toreturn

    return render_template("index.html")

@app.route('/triangle')
def triangle():
	return render_template("triangle.html")

@app.route('/rectangle')
def rectangle():
	return render_template("rectangle.html")

@app.route('/hexagon')
def hexagon():
	return render_template("hexagon.html")
