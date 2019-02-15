from PIL import Image
from io import StringIO 
from flask import Flask, render_template, request
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
app = Flask(__name__)
engine = create_engine( 'sqlite:///fresh_hostel_project.db', echo=False)
db = scoped_session(sessionmaker(bind=engine))
@app.route("/")
def success1():
    score = 3
    img = "/static/IMAGES/"+str(score)+".jpg"
    #img1 = db.execute("select * from custumer").fetchall()
    #img1
    #db.commit()
    return render_template("success1.html",img1= img)


if __name__ == '__main__':
    app.run(debug=True)
     
