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
        R301 = "No Beds Availables"
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
    vno = request.form.get("v_no")
    date2 = datetime.strptime(DOJ, "%Y-%m-%d")
    dl = []
    for i in range(int(date2.month),int(date2.month)+13):

      if int(i/12) > 0 and i%12 >= 0 and i>12:
        if  i%12==2 and date2.day>28:
            dl.append(date(date2.year+1,i%12,28))
        else:
            dl.append(date(date2.year+1,i%12,date2.day))
      else:
        if  i==2 and date2.day>28:
            dl.append(date(date2.year,i,28))
        else:
            dl.append(date(date2.year,i,date2.day))


               
    #imag1 = request.form.get("Image")
    #img = "/static/IMAGES/"+str(imag1)+".jpg"
   
    prev_id1 = db.execute("select max(id)+1 from custumer").fetchone()
    if prev_id1 == None:
        prev_id1 = 1
    img1 = request.form.get('fileupload')
    img = "/static/IMAGES/"+str(img1)
    db.execute("insert into custumer(id,name,f_name,doj,student_no,Adress,college,age,aadhar,parent_no,advance,room,email,imag,package,vehicle_no) values(:id,:name,:f_name,:doj,:student_no,:Adress,:college,:age,:aadhar,:parent_no,:advance,:room,:email,:imag,:package,:vehicle_no)", {"id":prev_id1[0],"name":sname,"f_name":fname,"doj":DOJ,"student_no":sphone,"Adress":Address,"college":college,"age":Age,"aadhar":Aadhar,"parent_no":fphone,"advance":Advance,"room":Room,"email":Email,"imag":img,"package":int(pack123),"vehicle_no":vno})
    for i in range(0,12):
        db.execute("insert into fee(id,actualdate,month,test) values(:id,:actualdate,:month,:test)",{"id":prev_id1[0],"actualdate":dl[i],"month":dl[i].month,"test":i+1})
        db.commit()
    return render_template("welcome.html")
@app.route("/select_custumer", methods = ["GET","POST"])
def search():
    inserted = db.execute("select * from custumer").fetchall()
    return render_template("insert.html",insert = inserted)
@app.route("/add_fee",methods=["GET","POST"])    
def add_fee():
    names = db.execute("select name from custumer").fetchall()
    return render_template('fees1.html',nam = names)
@app.route("/addfee",methods=["GET","POST"])    
def add_fee1():
    feename1 = request.form.get("feename")
    cust = db.execute("select * from custumer where name = :name",{"name":feename1}).fetchall()
    return render_template("disfee.html",insert = cust)
@app.route('/addfee2',methods=["GET","POST"])
def add_fee2():
    id1 = request.form.get("select123")
    see = db.execute("select id,name,package,doj from custumer where id= :id",{"id":id1}).fetchone()
    bal1 = db.execute("select sum(balance) from fee where id = :id",{"id":id1}).fetchone()
    return render_template('add12.html',see1 = see,totbal = bal1[0])

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
    return render_template('welcome.html')
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
     dict1 = {}
     id1 = request.form.get("select123")
     search2 = db.execute("select * from custumer where id = :id",{"id":id1}).fetchone()
     smon1 = db.execute("select * from fee where id = :id and month=:month",{"id":id1,"month":1}).fetchone()
     smon2 = db.execute("select * from fee where id = :id and month=:month",{"id":id1,"month":2}).fetchone()
     smon3 = db.execute("select * from fee where id = :id and month=:month",{"id":id1,"month":3}).fetchone()
     smon4 = db.execute("select * from fee where id = :id and month=:month",{"id":id1,"month":4}).fetchone()
     smon5 = db.execute("select * from fee where id = :id and month=:month",{"id":id1,"month":5}).fetchone()
     smon6 = db.execute("select * from fee where id = :id and month=:month",{"id":id1,"month":6}).fetchone()
     smon7 = db.execute("select * from fee where id = :id and month=:month",{"id":id1,"month":7}).fetchone()
     smon8 = db.execute("select * from fee where id = :id and month=:month",{"id":id1,"month":8}).fetchone()
     smon9 = db.execute("select * from fee where id = :id and month=:month",{"id":id1,"month":9}).fetchone()
     smon10 = db.execute("select * from fee where id = :id and month=:month",{"id":id1,"month":10}).fetchone()
     smon11 = db.execute("select * from fee where id = :id and month=:month",{"id":id1,"month":11}).fetchone()
     smon12 = db.execute("select * from fee where id = :id and month=:month",{"id":id1,"month":12}).fetchone()
     tot_balan =db.execute("select sum(balance) from fee where id = :id",{"id":id1}).fetchone()
     return render_template('filter.html',nam=search2,m1=smon1,m2=smon2,m3=smon3,m4=smon4,m5=smon5,
        m6=smon6,m7=smon7,m8=smon8,m9=smon9,m10=smon10,m11=smon11,m12=smon12,t_bal=tot_balan[0])
@app.route("/updcus00",methods=["GET","POST"])    
def upcus():
    return render_template('upcus001.html')
@app.route("/updcus01",methods=["GET","POST"])    
def upcus01():
    feename1 = request.form.get("feename")
    cust = db.execute("select * from custumer where name = :name",{"name":feename1}).fetchall()
    return render_template("upcus002.html",insert = cust)
@app.route("/updcus02",methods = ["GET","POST"])
def upcus02():
    id3 = request.form.get('select123')
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
    vno = request.form.get("v_no")
    date2 = datetime.strptime(DOJ, "%Y-%m-%d")
    dp = []
    for i in range(int(date2.month),int(date2.month)+13):
      if int(i/12) > 0 and i%12 > 0 and i>12:
        if  i%12==2 and date2.day>28:
            dp.append(date(date2.year+1,i%12,28))
        else:
            dp.append(date(date2.year+1,i%12,date2.day))
      else:
        if  i==2 and date2.day>28:
            dp.append(date(date2.year,i,28))
        else:
            dp.append(date(date2.year,i,date2.day))
    db.execute("update custumer set name=:name,f_name=:f_name,doj=:doj,student_no=:student_no,Adress=:Adress,college=:college,age=:age,aadhar=:aadhar,parent_no=:parent_no,advance=:advance,room=:room,email=:email,package=:package,vehicle_no=:vehicle_no where id=:id",{"name":sname,"f_name":fname,"doj":DOJ,"student_no":sphone,"Adress":Address,"college":college,"age":Age,"aadhar":Aadhar,"parent_no":fphone,"advance":Advance,"room":Room,"email":Email,"package":int(pack123),"vehicle_no":vno,"id":id8})
    for i in range(0,12):
        db.execute("update fee set actualdate=:actualdate,month=:month where id=:id and test=:test",{"actualdate":dp[i],"month":dp[i].month,"id":id8,"test":i+1})
        db.commit()
    '''for i in range(0,12):
        db.execute("insert into fee(id,actualdate,month,test) values(:id,:actualdate,:month,:test)",{"id":id8,"actualdate":dp[i],"month":dp[i].month,"test":i+1})
        db.commit()'''    
    return render_template("welcome.html")
@app.route("/delcus00",methods=["GET","POST"])    
def delet():
    return render_template('delet001.html')
@app.route("/delcus01",methods=["GET","POST"])    
def delet01():
    feename1 = request.form.get("feename")
    cust = db.execute("select * from custumer where name = :name",{"name":feename1}).fetchall()
    return render_template("delet002.html",insert = cust)    
@app.route("/deletecus",methods=["GET","POST"])
def delet02():
    id5 = request.form.get("select123")
    db.execute("delete from custumer where id=:id",{"id":id5})
    db.execute("delete from fee where id = :id",{"id":id5})
    db.commit()
    return render_template("welcome.html")
@app.route("/upfees",methods = ["GET","POST"])
def upfe():
       return render_template('updfee.html')
@app.route("/upfee1",methods=["GET","POST"])    
def upd_fee1():
    feename1 = request.form.get("feename")
    cust = db.execute("select * from custumer where name = :name",{"name":feename1}).fetchall()
    return render_template("updfee1.html",insert = cust)
@app.route('/upfee2',methods=["GET","POST"])
def upd_fee2():
    id1 = request.form.get("select123")
    mon = request.form.get("monthy")
    if mon == "january":
        mon1 = 1
    elif mon == "febraury":
        mon1 = 2
    elif mon == "march":
        mon1 = 3   
    elif mon == "april":
        mon1 = 4
    elif mon == "may":
        mon1 = 5
    elif mon == "june":
        mon1 = 6
    elif mon == "july":
        mon1 = 7
    elif mon == "august":
        mon1 = 8
    elif mon == "september":
        mon1 = 9
    elif mon == "october":
        mon1 = 10
    elif mon == "november":
        mon1 = 11
    elif mon == "december":
        mon1 = 12
    see = db.execute("select id,name,package,doj from custumer where id = :id",{"id":id1}).fetchone()
    seew = db.execute("select id,actualdate,paiddate,feepaid,modeofpayement,remarks from fee where id = :id and month = :month",{"id":id1,"month":mon1}).fetchone()
    bal1 = db.execute("select sum(balance) from fee where id = :id",{"id":id1}).fetchone()
    return render_template('updfee2.html',see1 = see,totbal = bal1[0],see2 = seew)

@app.route('/searchbalance1',methods= ["GET","POST"])
def search_bal1():
    return render_template("test_search.html")
@app.route('/searchbymonth',methods = ["GET","POST"])
def search_bymonth():
    mon = request.form.get("monthly")
    if mon == "january":
        mon1 = 1
    elif mon == "febraury":
        mon1 = 2
    elif mon == "march":
        mon1 = 3   
    elif mon == "april":
        mon1 = 4
    elif mon == "may":
        mon1 = 5
    elif mon == "june":
        mon1 = 6
    elif mon == "july":
        mon1 = 7
    elif mon == "august":
        mon1 = 8
    elif mon == "september":
        mon1 = 9
    elif mon == "october":
        mon1 = 10
    elif mon == "november":
        mon1 = 11
    elif mon == "december":
        mon1 = 12
    allinone = db.execute("select custumer.id,name,actualdate,paiddate,feepaid,modeofpayement,remarks,balance from custumer join fee on custumer.id = fee.id where month = :month ",{"month":mon1}).fetchall()        
    return render_template("test_search2.html",every = allinone)
@app.route('/searchbytotbal',methods = ["GET","POST"])
def search_bytotbal():
    test = request.form.get("searchname")
    if test == 'total' or test == 'TOTAL':
        t1 = db.execute("select custumer.id as id,name,sum(balance) as maxy from fee join custumer on fee.id = custumer.id group by fee.id").fetchall()
        return render_template("search_tot_bal.html",insert = t1)

@app.route('/searchbydate1',methods = ["GET","POST"])
def search_bydate1():
    return render_template('search_by_date.html')
@app.route('/searchbydate',methods = ["GET","POST"])
def search_bydate():
    #searchdate = request.form.get("doj")
    #date21 = datetime.strptime(DOJ, "%Y-%m-%d")

    allones = db.execute("select * from custumer join fee on custumer.id = fee.id where  strftime('%d','now') - strftime('%d',actualdate) > 0 and strftime('%m',actualdate) = strftime('%m','now') and feepaid = 0").fetchall()
    al = db.execute("select count(*) from custumer join fee on custumer.id = fee.id where  strftime('%d','now') - strftime('%d',actualdate) > 0 and strftime('%m',actualdate) = strftime('%m','now') and feepaid = 0").fetchone()

    return render_template("allones.html",allone = allones,count = al)

@app.route('/searchbyroom',methods = ["GET","POST"])
def search_byroom():
    return render_template("roomname.html")
@app.route('/searchbyroom1',methods = ["GET","POST"])
def search_byroom1():
    roomno = request.form.get('searchname')
    count = db.execute("select count(*) from custumer where room = :room",{"room":int(roomno)}).fetchone()
    insert = db.execute("select * from custumer where room = :room",{"room":int(roomno)}).fetchall()
    return render_template('roomname1.html',insert = insert,count = count)

if __name__ == "__main__":
    app.run(debug=True)