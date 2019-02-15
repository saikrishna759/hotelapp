import os
import smtplib
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def trail():
	return render_template("email.html")
@app.route('/register', methods = ["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")	
    message = "HI S5J , your problem statement ie.. hospital finder is selected for finals,so check your status through your spoc and get ready for the competition and try to implement so many things in your project....lol(hi ra idi flask nunchi pampina....)"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("sih2019problem@gmail.com","sih@2019@problem")
    server.sendmail("sai.sanniboina@gmail.com",email,message)
    return render_template("success1.html")
if __name__ == "__main__":
	app.run(debug=True)