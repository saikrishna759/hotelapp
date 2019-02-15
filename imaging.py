from flask import Flask, render_template, request
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
app = Flask(__name__)
engine = create_engine( 'sqlite:///fresh_hostel_project.db', echo=False)
db = scoped_session(sessionmaker(bind=engine))
@app.route("/")
def index():
	inserted = db.execute("select * from custumer").fetchall()
	db.commit()
	num = 1
	return render_template("insert.html",insert=inserted,number=num)
if __name__ == "__main__" :
	app.run(debug=True)