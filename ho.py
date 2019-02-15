import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from flask import Flask, render_template, request

app = Flask(__name__)

engine = create_engine( 'sqlite:///hosdb.db', echo=False)
db = scoped_session(sessionmaker(bind=engine))
@app.route("/")
def index():
	hospitals = db.execute("select * from hospital").fetchall()
	return render_template("index2.html",hospital = hospitals)
@app.route("/set",methods = ["POST"])	
def set():
	name = request.form.get("name")
	hospital_id = request.form.get("hospital_id")
	db.execute("insert into doctors(name,hospital_id) values(:name,:hospital_id)",{"name":name,"hospital_id":hospital_id})
	doctor = db.execute("select * from doctors").fetchall()
	db.commit()
	return render_template('success.html',doctors=doctor)

if __name__ == "__main__":
	app.run(debug=True)
