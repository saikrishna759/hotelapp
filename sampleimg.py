import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from flask import Flask, render_template, request

app = Flask(__name__)

engine = create_engine( 'sqlite:///fresh_hostel_project.db', echo=False)
db = scoped_session(sessionmaker(bind=engine))
@app.route("/")
def index():
	custumers = db.execute("select id, name, balance from custumer group by id having balance>0 order by balance desc").fetchall()
	return render_template("index21.html",custumers = custumers)

if __name__ == "__main__":
	app.run(debug=True)

