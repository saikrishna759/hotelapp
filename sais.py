from flask import Flask, render_template, request

app = Flask(__name__)
notes = []


@app.route('/', methods=["GET", "POST"])
def index1():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("index1.html", notes=notes)




if __name__ == "__main__":
    app.run(debug=True)
