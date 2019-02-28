from flask import Flask, render_template, request
import os
from datetime import date,datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is secret key'
engine = create_engine( 'sqlite:///fresh_hostel_project.db', echo=False)
db = scoped_session(sessionmaker(bind=engine))
username1 = "saikrishna"
password1 = "saikrishna"
dl = []
class loginform(FlaskForm):
    username = StringField('username',validators = [InputRequired('username is required')])
    password = PasswordField('password',validators = [InputRequired('password is required')])

@app.route("/")
def index():
    form = loginform()
    #if form.validate_on_submit():
    #return render_template('welcome.html',name = form.username.data)
    #else:
    return render_template('login1.html',form = form)
@app.route("/welcome", methods=["POST"])
def welcome():

        name = request.form.get("username")
        pswd = request.form.get("password")
        if name==username1 and pswd==password1: 
                return render_template("welcome.html", name = name.upper())
        else:
          form = loginform()    
          return render_template('login1.html',form=form, name = 'invalid login') 
@app.route("/add_custumer", methods = ["GET","POST"])
def add():
    prev_id = db.execute("select max(id)+1 from custumer").fetchone()
    c101 = db.execute("select count(room) from custumer where room = 101").fetchone()
    c102 = db.execute("select count(room) from custumer where room = 102").fetchone()
    c103 = db.execute("select count(room) from custumer where room = 103").fetchone()
    c201 = db.execute("select count(room) from custumer where room = 201").fetchone()
    c202 = db.execute("select count(room) from custumer where room = 202").fetchone()
    c203 = db.execute("select count(room) from custumer where room = 203").fetchone()
    c301 = db.execute("select count(room) from custumer where room = 301").fetchone()
    c302 = db.execute("select count(room) from custumer where room = 302").fetchone()
    c303 = db.execute("select count(room) from custumer where room = 303").fetchone()
    #101
    if (10 - c101[0])>0:
        R101 = str(10- c101[0])+" Beds Available"
    else:
        R101 = "No Beds Available"
    #102    
    if (10 - c102[0])>0:
        R102 = str(10-c102[0])+" Beds Available"
    else:
        R102 = "No Beds Available"  
    #103     
    if (10 - c103[0])>0:
        R103 = str(10- c103[0])+" Beds Available"
    else:
        R103 = "No Beds Available"
    #201   
    if (10 - c201[0])>0:
        R201 = str(10-c201[0])+" Beds Available"
    else:
        R201 = "No Beds Available"    
    #202    
    if (10 - c202[0])>0:
        R202 = str(10- c202[0])+" Beds Available"
    else:
        R202 = "No Beds Available"
    #203    
    if (10 - c203[0])>0:
        R203 = str(10-c203[0])+" Beds Available"
    else:
        R203 = "No Beds Available"
    #301       
    if (5 - c301[0])>0:
        R301 = str(5- c301[0])+" Beds Available"
    else:
        R301 = "No Beds Available"
    #302    
    if (5 - c302[0])>0:
        R302 = str(5-c302[0])+" Beds Available"
    else:
        R302 = "No Beds Available"
    #303    
    if (5 - c303[0])>0:
        R303 = str(5-c303[0])+" Beds Available"
    else:
        R303 = "No Beds Available"                
    
    return render_template("trail.html",prev_id = prev_id[0],R101 = R101,R102 = R102,R103=R103,R201 = R201,R202 = R202,R203=R203,R301 = R301,R302 = R302,R303=R303)
@app.route("/insert",methods = ["POST"])
def insert():
    sname  = request.form.get("name")
    fname = request.form.get("f_name")
    sphone = request.form.get("Sphone")
    fphone = request.form.get("Fphone")
    DOJ = request.form.get("doj")
    college = request.form.get("college")
    Aadhar = request.form.get("Aadhar")
    Age = request.form.get("age")
    id1 = request.form.get("Image")
    Email = request.form.get("email")
    Address = request.form.get("address")
    Advance = request.form.get("advance")
    Room = request.form.get("room")
    pack123 = request.form.get("fee_package")
    c101 = db.execute("select count(room) from custumer where room = 101")
    c102 = db.execute("select count(room) from custumer where room = 102")
    date2 = datetime.strptime(DOJ, "%Y-%m-%d")
    dl.append(date(date2.year,1,date2.day))
    dl.append(date(date2.year,2,date2.day))
    dl.append(date(date2.year,3,date2.day))
    dl.append(date(date2.year,4,date2.day))
    dl.append(date(date2.year,5,date2.day))
    dl.append(date(date2.year,6,date2.day))
    dl.append(date(date2.year,7,date2.day))
    dl.append(date(date2.year,8,date2.day))
    dl.append(date(date2.year,9,date2.day))
    dl.append(date(date2.year,10,date2.day))
    dl.append(date(date2.year,11,date2.day))
    dl.append(date(date2.year,12,date2.day))
    #imag1 = request.form.get("Image")
    #img = "/static/IMAGES/"+str(imag1)+".jpg"
    prev_id1 = db.execute("select max(id)+1 from custumer").fetchone()
    img = "/static/IMAGES/"+str(prev_id1[0])+".jpg"
    db.execute("insert into custumer(id,name,f_name,doj,student_no,Adress,college,age,aadhar,parent_no,advance,room,email,imag,package) values(:id,:name,:f_name,:doj,:student_no,:Adress,:college,:age,:aadhar,:parent_no,:advance,:room,:email,:imag,:package)", {"id":prev_id1[0],"name":sname,"f_name":fname,"doj":DOJ,"student_no":sphone,"Adress":Address,"college":college,"age":Age,"aadhar":Aadhar,"parent_no":fphone,"advance":Advance,"room":Room,"email":Email,"imag":img,"package":int(pack123)})
    #inserted = db.execute("select * from custumer").fetchall()
    for i in range(0,12):
        db.execute("insert into fee(id,actualdate,month) values(:id,:actualdate,:month)",{"id":prev_id1[0],"actualdate":dl[i],"month":dl[i].month})
        db.commit()
    return render_template("welcome.html")
@app.route("/select_custumer", methods = ["GET","POST"])
def search():
    inserted = db.execute("select * from custumer").fetchall()
    return render_template("insert.html",insert = inserted)
@app.route("/add_fee",methods=["GET","POST"])    
def add_fee():
   # feename = request.form.get('newfee')
    #cust = db.execute("select id,name,doj,student_no,parent_no,advance,room,balance,packages from custumer join fee on custumer.id = fee.id where name = :name",{"name":feename})
    return render_template('fees1.html')
@app.route("/addfee",methods=["GET","POST"])    
def add_fee1():
    feename1 = request.form.get("feename")
    #cust = db.execute("select custumer.id,custumer.name,custumer.doj,custumer.student_no,custumer.parent_no,custumer.advance,custumer.room,fee.balance,fee.packages from custumer  join fee on custumer.id = fee.id where name = :name",{"name":feename1}).fetchall()
    cust = db.execute("select * from custumer where name = :name",{"name":feename1}).fetchall()
    #cust1 = db.execute("select * from custumer join fee").fetchall()
    return render_template("disfee.html",insert = cust)
@app.route('/addfee2',methods=["GET","POST"])
def add_fee2():
    id1 = request.form.get("select123")
    see = db.execute("select id,name,package,doj from custumer where id= :id",{"id":id1}).fetchone()
    bal1 = db.execute("select balance from fee where id = :id and month=:month",{"id":id1,"month":1}).fetchone()
    bal2 = db.execute("select balance from fee where id = :id and month=:month",{"id":id1,"month":2}).fetchone()
    bal3 = db.execute("select balance from fee where id = :id and month=:month",{"id":id1,"month":3}).fetchone()
    bal4 = db.execute("select balance from fee where id = :id and month=:month",{"id":id1,"month":4}).fetchone()
    bal5 = db.execute("select balance from fee where id = :id and month=:month",{"id":id1,"month":5}).fetchone()
    bal6 = db.execute("select balance from fee where id = :id and month=:month",{"id":id1,"month":6}).fetchone()
    bal7 = db.execute("select balance from fee where id = :id and month=:month",{"id":id1,"month":7}).fetchone()
    bal8 = db.execute("select balance from fee where id = :id and month=:month",{"id":id1,"month":8}).fetchone()
    bal9 = db.execute("select balance from fee where id = :id and month=:month",{"id":id1,"month":9}).fetchone()
    bal10 = db.execute("select balance from fee where id = :id and month=:month",{"id":id1,"month":10}).fetchone()
    bal11 = db.execute("select balance from fee where id = :id and month=:month",{"id":id1,"month":11}).fetchone()
    bal12 = db.execute("select balance from fee where id = :id and month=:month",{"id":id1,"month":12}).fetchone()     
    total_balance = int(int(bal1[0])+int(bal2[0])+int(bal3[0])+int(bal4[0])+int(bal5[0])+int(bal6[0])
                    +int(bal7[0])+int(bal8[0])+int(bal9[0])+int(bal10[0])+int(bal11[0])+int(bal12[0]))
    return render_template('add12.html',see1 = see,totbal = total_balance)

@app.route('/welcome1',methods=["GET","POST"])
def add_fee3():
    feeid = request.form.get("fee_id")
    pack =  request.form.get("fee_pack")
    fee_bal =  request.form.get("fee_balance")
    feepaid  = request.form.get("fee_paid")
    remarked = request.form.get("remark")
    upd_bal = request.form.get("up_bal")
    modofpay =  request.form.get("mop")
    
   
    if int(pack)==1:
        fixedfee = 4000
    elif int(pack)==6:
        fixedfee = 22000
    elif int(pack)==12:
        fixedfee = 38000
    if upd_bal:
        feebalance = upd_bal
    else:
        feebalance  = fixedfee - int(feepaid)                    
    paydate = request.form.get("dop")
    date0 = datetime.strptime(paydate, "%Y-%m-%d")
    date1 = date(date0.year,date0.month,date0.day)
    db.execute("update fee set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayement=:modeofpayment,remarks=:remarks where id=:id and month=:month",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid),"month":date0.month})
    db.commit()   
    return render_template('welcome1.html',paid = date1)
@app.route('/byname',methods=["GET","POST"])
def by_name():
    return render_template('byname.html')
@app.route('/dispalysearch',methods=["GET","POST"])
def display_search():
    dname = request.form.get("searchname")
    search1 = db.execute("select * from custumer where name = :name",{"name":dname}).fetchall()
    return render_template("displaysearch1.html",insert = search1)
@app.route('/dispalysearch2',methods=["GET","POST"])
def display_search2():
     id1 = request.form.get("select123")
     search2 = db.execute("select * from custumer where id = :id",{"id":id1}).fetchone()
     smon1 = db.execute("select * from fee where id = :id,month=:month",{"id":id1,"month":1}).fetchone()
     smon2 = db.execute("select * from fee where id = :id,month=:month",{"id":id1,"month":2}).fetchone()
     smon3 = db.execute("select * from fee where id = :id,month=:month",{"id":id1,"month":3}).fetchone()
     smon4 = db.execute("select * from fee where id = :id,month=:month",{"id":id1,"month":4}).fetchone()
     smon5 = db.execute("select * from fee where id = :id,month=:month",{"id":id1,"month":5}).fetchone()
     smon6 = db.execute("select * from fee where id = :id,month=:month",{"id":id1,"month":6}).fetchone()
     smon7 = db.execute("select * from fee where id = :id,month=:month",{"id":id1,"month":7}).fetchone()
     smon8 = db.execute("select * from fee where id = :id,month=:month",{"id":id1,"month":8}).fetchone()
     smon9 = db.execute("select * from fee where id = :id,month=:month",{"id":id1,"month":9}).fetchone()
     smon10 = db.execute("select * from fee where id = :id,month=:month",{"id":id1,"month":10}).fetchone()
     smon11 = db.execute("select * from fee where id = :id,month=:month",{"id":id1,"month":11}).fetchone()
     smon12 = db.execute("select * from fee where id = :id,month=:month",{"id":id1,"month":12}).fetchone()
     tot_balan =int(smon1[1])+int(smon2[1])+int(smon3[1])+int(smon4[1])+int(smon5[1])+ int(smon6[1])+int(smon7[1])+int(smon8[1])+int(smon9[1])+int(smon10[1])+int(smon11[1])+int(smon12[1])
     return render_template('filter.html',nam=search2,m1=smon1,m2=smon2,m3=smon3,m4=smon4,m5=smon5,
        m6=smon6,m7=smon7,m8=smon8,m9=smon9,m10=smon10,m11=smon11,m12=smon12,t_bal=tot_balan)

@app.route("/updatecus",methods = ["GET","POST"])
def upcus():
    id3 = 25
    det = db.execute("select * from custumer where id= :id",{"id":id3}).fetchone()
    c101 = db.execute("select count(room) from custumer where room = 101").fetchone()
    c102 = db.execute("select count(room) from custumer where room = 102").fetchone()
    c103 = db.execute("select count(room) from custumer where room = 103").fetchone()
    c201 = db.execute("select count(room) from custumer where room = 201").fetchone()
    c202 = db.execute("select count(room) from custumer where room = 202").fetchone()
    c203 = db.execute("select count(room) from custumer where room = 203").fetchone()
    c301 = db.execute("select count(room) from custumer where room = 301").fetchone()
    c302 = db.execute("select count(room) from custumer where room = 302").fetchone()
    c303 = db.execute("select count(room) from custumer where room = 303").fetchone()
    #101
    if (10 - c101[0])>0:
        R101 = str(10- c101[0])+" Beds Available"
    else:
        R101 = "No Beds Available"
    #102    
    if (10 - c102[0])>0:
        R102 = str(10-c102[0])+" Beds Available"
    else:
        R102 = "No Beds Available"  
    #103     
    if (10 - c103[0])>0:
        R103 = str(10- c103[0])+" Beds Available"
    else:
        R103 = "No Beds Available"
    #201   
    if (10 - c201[0])>0:
        R201 = str(10-c201[0])+" Beds Available"
    else:
        R201 = "No Beds Available"    
    #202    
    if (10 - c202[0])>0:
        R202 = str(10- c202[0])+" Beds Available"
    else:
        R202 = "No Beds Available"
    #203    
    if (10 - c203[0])>0:
        R203 = str(10-c203[0])+" Beds Available"
    else:
        R203 = "No Beds Available"
    #301       
    if (5 - c301[0])>0:
        R301 = str(5- c301[0])+" Beds Available"
    else:
        R301 = "No Beds Available"
    #302    
    if (5 - c302[0])>0:
        R302 = str(5-c302[0])+" Beds Available"
    else:
        R302 = "No Beds Available"
    #303    
    if (5 - c303[0])>0:
        R303 = str(5-c303[0])+" Beds Available"
    else:
        R303 = "No Beds Available"  
    return render_template("uptade.html",det = det,R101 = R101,R102 = R102,R103=R103,R201 = R201,R202 = R202,R203=R203,R301 = R301,R302 = R302,R303=R303)

@app.route("/updatecus1",methods = ["GET","POST"])
def upcus2():
    id8  = request.form.get("identity")
    sname  = request.form.get("name")
    fname = request.form.get("f_name")
    sphone = request.form.get("Sphone")
    fphone = request.form.get("Fphone")
    DOJ = request.form.get("doj")
    college = request.form.get("college")
    Aadhar = request.form.get("Aadhar")
    Age = request.form.get("age")
    Email = request.form.get("email")
    Address = request.form.get("address")
    Advance = request.form.get("advance")
    Room = request.form.get("room")
    pack123 = request.form.get("fee_package")
    db.execute("update custumer set name=:name,f_name=:f_name,doj=:doj,student_no=:student_no,Adress=:Adress,college=:college,age=:age,aadhar=:aadhar,parent_no=:parent_no,advance=:advance,room=:room,email=:email,package=:package where id=:id",{"name":sname,"f_name":fname,"doj":DOJ,"student_no":sphone,"Adress":Address,"college":college,"age":Age,"aadhar":Aadhar,"parent_no":fphone,"advance":Advance,"room":Room,"email":Email,"package":int(pack123),"id":id8})
    db.commit()
    return render_template("welcome.html")
@app.route("/deletecus",methods=["GET","POST"])
def delet():
    id5 = 525
    db.execute("delete from custumer where id=:id",{"id":id5})
    db.commit()
    return render_template("welcome.html")
if __name__ == "__main__":
    app.run(debug=True)