from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index4.html")

@app.route('/hell', methods = ["POST"])
def hell():
	name = request.form.get("name")
	return render_template("int.html", name = name)


if __name__ == "__main__":
    app.run(debug=True)    