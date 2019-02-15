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
    d1 = date(int(date2.year),1,int(date2.day))
    d2 = date(date2.year,2,date2.day)
    d3 = date(date2.year,3,date2.day)
    d4 = date(date2.year,4,date2.day)
    d5 = date(date2.year,5,date2.day)
    d6 = date(date2.year,6,date2.day)
    d7 = date(date2.year,7,date2.day)
    d8 = date(date2.year,8,date2.day)
    d9 = date(date2.year,9,date2.day)
    d10 = date(date2.year,10,date2.day)
    d11 = date(date2.year,11,date2.day)
    d12 = date(date2.year,12,date2.day)
    
    

    




    #imag1 = request.form.get("Image")
    #img = "/static/IMAGES/"+str(imag1)+".jpg"
    prev_id1 = db.execute("select max(id)+1 from custumer").fetchone()
    img = "/static/IMAGES/"+str(prev_id1[0])+".jpg"
    db.execute("insert into custumer(id,name,f_name,doj,student_no,Adress,college,age,aadhar,parent_no,advance,room,email,imag,package) values(:id,:name,:f_name,:doj,:student_no,:Adress,:college,:age,:aadhar,:parent_no,:advance,:room,:email,:imag,:package)", {"id":prev_id1[0],"name":sname,"f_name":fname,"doj":DOJ,"student_no":sphone,"Adress":Address,"college":college,"age":Age,"aadhar":Aadhar,"parent_no":fphone,"advance":Advance,"room":Room,"email":Email,"imag":img,"package":int(pack123)})
    #inserted = db.execute("select * from custumer").fetchall()
    db.execute("insert into jan(id,actualdate) values(:id,:actualdate)",{"id":prev_id1[0],"actualdate":d1})
    db.execute("insert into feb(id,actualdate) values(:id,:actualdate)",{"id":prev_id1[0],"actualdate":d2})
    db.execute("insert into mar(id,actualdate) values(:id,:actualdate)",{"id":prev_id1[0],"actualdate":d3})
    db.execute("insert into apr(id,actualdate) values(:id,:actualdate)",{"id":prev_id1[0],"actualdate":d4})
    db.execute("insert into may(id,actualdate) values(:id,:actualdate)",{"id":prev_id1[0],"actualdate":d5})
    db.execute("insert into jun(id,actualdate) values(:id,:actualdate)",{"id":prev_id1[0],"actualdate":d6})
    db.execute("insert into jul(id,actualdate) values(:id,:actualdate)",{"id":prev_id1[0],"actualdate":d7})
    db.execute("insert into agus(id,actualdate) values(:id,:actualdate)",{"id":prev_id1[0],"actualdate":d8})
    db.execute("insert into sept(id,actualdate) values(:id,:actualdate)",{"id":prev_id1[0],"actualdate":d9})
    db.execute("insert into oct(id,actualdate) values(:id,:actualdate)",{"id":prev_id1[0],"actualdate":d10})
    db.execute("insert into nov(id,actualdate) values(:id,:actualdate)",{"id":prev_id1[0],"actualdate":d11})
    db.execute("insert into dec(id,actualdate) values(:id,:actualdate)",{"id":prev_id1[0],"actualdate":d12})
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
    #see = db.execute("select custumer.id,custumer.name,fee.id,fee.balance from custumer join fee on custumer.id= fee.id where custumer.id  = :id",{"id":id1}).fetchone()
    see = db.execute("select id,name,package,doj from custumer where id= :id",{"id":id1}).fetchone()
    bal1 = db.execute("select balance from jan where id = :id",{"id":id1}).fetchone()
    bal2 = db.execute("select balance from feb where id = :id",{"id":id1}).fetchone()
    bal3 = db.execute("select balance from mar where id = :id",{"id":id1}).fetchone()
    bal4 = db.execute("select balance from apr where id = :id",{"id":id1}).fetchone()
    bal5 = db.execute("select balance from may where id = :id",{"id":id1}).fetchone()
    bal6 = db.execute("select balance from jun where id = :id",{"id":id1}).fetchone()
    bal7 = db.execute("select balance from jul where id = :id",{"id":id1}).fetchone()
    bal8 = db.execute("select balance from agus where id = :id",{"id":id1}).fetchone()
    bal9 = db.execute("select balance from sept where id = :id",{"id":id1}).fetchone()
    bal10 = db.execute("select balance from oct where id = :id",{"id":id1}).fetchone()
    bal11 = db.execute("select balance from nov where id = :id",{"id":id1}).fetchone()
    bal12 = db.execute("select balance from dec where id = :id",{"id":id1}).fetchone()
    total_balance =int(bal1[0])+int(bal2[0])+int(bal3[0])+int(bal4[0])+int(bal5[0])+ int(bal6[0])+int(bal7[0])+int(bal8[0])+int(bal9[0])+int(bal10[0])+int(bal11[0])+int(bal12[0])

    return render_template('add12.html',see1 = see,totbal = total_balance)

@app.route('/welcome1',methods=["GET","POST"])
def add_fee3():
    feeid = request.form.get("fee_id")
    pack =  request.form.get("fee_pack")
    fee_bal =  request.form.get("fee_balance")
    feepaid  = request.form.get("fee_paid")
    remarked = request.form.get("remark")
    modofpay =  request.form.get("mop")
    
   
    if int(pack)==1:
        fixedfee = 4000
    elif int(pack)==6:
        fixedfee = 22000
    elif int(pack)==12:
        fixedfee  = 38000
    feebalance  = fixedfee - int(feepaid)               
    paydate = request.form.get("dop")
    date0 = datetime.strptime(paydate, "%Y-%m-%d")
    date1 = date(date0.year,date0.month,date0.day)
    if date0.month==1:
        db.execute("update jan set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayment=:modeofpayment,remarks=:remarks where id=:id",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid)})
        db.commit()
    elif date0.month==2:
        db.execute("update feb set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayment=:modeofpayment,remarks=:remarks  where id=:id",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid)})
        db.commit()
    elif date0.month==3:
        db.execute("update mar set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayment=:modeofpayment,remarks=:remarks  where id=:id",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid)})
        db.commit()
    elif date0.month==4:
        db.execute("update apr set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayment=:modeofpayment,remarks=:remarks  where id=:id",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid)})
        db.commit()
    elif date0.month==5:
        db.execute("update may set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayment=:modeofpayment,remarks=:remarks  where id=:id",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid)})
        db.commit()
    elif date0.month==6:
        db.execute("update jun set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayment=:modeofpayment,remarks=:remarks  where id=:id",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid)})
        db.commit()
    elif date0.month==7:
        db.execute("update jul set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayment=:modeofpayment,remarks=:remarks  where id=:id",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid)})
        db.commit()
    elif date0.month==8:
        db.execute("update agus set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayment=:modeofpayment,remarks=:remarks  where id=:id",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid)})
        db.commit()
    elif date0.month==9:
        db.execute("update sept set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayment=:modeofpayment,remarks=:remarks  where id=:id",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid)})
        db.commit()
    elif date0.month==10:
        db.execute("update oct set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayment=:modeofpayment,remarks=:remarks  where id=:id",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid)})
        db.commit()
    elif date0.month==11:
        db.execute("update nov set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayment=:modeofpayment,remarks=:remarks  where id=:id",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid)})
        db.commit()
    elif date0.month==12:
        db.execute("update dec set balance=:balance,feepaid=:feepaid,paiddate=:paiddate,modeofpayment=:modeofpayment,remarks=:remarks  where id=:id",{"balance":feebalance,"feepaid":feepaid,"paiddate":date1,"modeofpayment":modofpay,"remarks":remarked,"id":int(feeid)})
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
     smon1 = db.execute("select * from jan where id = :id",{"id":id1}).fetchone()
     smon2 = db.execute("select id,balance,actualdate,paiddate,feepaid from feb where id = :id",{"id":id1}).fetchone()
     smon3 = db.execute("select * from mar where id = :id",{"id":id1}).fetchone()
     smon4 = db.execute("select * from apr where id = :id",{"id":id1}).fetchone()
     smon5 = db.execute("select * from may where id = :id",{"id":id1}).fetchone()
     smon6 = db.execute("select * from jun where id = :id",{"id":id1}).fetchone()
     smon7 = db.execute("select * from jul where id = :id",{"id":id1}).fetchone()
     smon8 = db.execute("select * from agus where id = :id",{"id":id1}).fetchone()
     smon9 = db.execute("select * from sept where id = :id",{"id":id1}).fetchone()
     smon10 = db.execute("select * from oct where id = :id",{"id":id1}).fetchone()
     smon11 = db.execute("select * from nov where id = :id",{"id":id1}).fetchone()
     smon12 = db.execute("select * from dec where id = :id",{"id":id1}).fetchone()
     tot_balan =int(smon1[1])+int(smon2[1])+int(smon3[1])+int(smon4[1])+int(smon5[1])+ int(smon6[1])+int(smon7[1])+int(smon8[1])+int(smon9[1])+int(smon10[1])+int(smon11[1])+int(smon12[1])
     return render_template('filter.html',nam=search2,m1=smon1,m2=smon2,m3=smon3,m4=smon4,m5=smon5,
        m6=smon6,m7=smon7,m8=smon8,m9=smon9,m10=smon10,m11=smon11,m12=smon12,t_bal=tot_balan)

if __name__ == "__main__":
    app.run(debug=True)