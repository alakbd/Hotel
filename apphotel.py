from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask_cors import CORS
import json
import datetime
mysql = MySQL()
app = Flask(__name__)
CORS(app)
# My SQL Instance configurations
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'webUser'
app.config['MYSQL_PASSWORD'] = 'webUserPass'
app.config['MYSQL_DB'] = 'hotel'
app.config['MYSQL_HOST'] = 'localhost' #Use IP
mysql.init_app(app)

@app.route("/addCustomer",methods=["POST"]) #Add Customer
def addCustomer():
  custName = request.args.get('name')
  email = request.args.get('email')
  phone = request.args.get('phone')
  address = request.args.get('address')
  TypePId = request.args.get('TypePId')
  cur = mysql.connection.cursor() #create a connection to the SQL instance
  s='''INSERT INTO customerTbl(custName,email,phone,address,TypePId) VALUES('{}','{}','{}','{}','{}');'''.format(custName,email,phone,address,TypePId)
  cur.execute(s)
  mysql.connection.commit()

  return '{"Result":"Success"}'
@app.route("/") #Default - Show Data
def viewCustomer(): # Name of the method
  cur = mysql.connection.cursor() #create a connection to the SQL instance
  cur.execute('''SELECT * FROM customerTbl''') # execute an SQL statment
  rv = cur.fetchall() #Retreive all rows returend by the SQL statment
  Results=[]
  for row in rv: #Format the Output Results and add to return string
    Result={}
    Result['custName']=row[0].replace('\n',' ')
    Result['email']=row[1]
    Result['phone']=row[2]
    Result['address']=row[3]
    Result['TypeId']=row[4]
    Result['custID']=row[5]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format
@app.route("/bookingPage") #Default - Show Data
def bookingPage(): # Name of the method
  cur = mysql.connection.cursor() #create a connection to the SQL instance
  cur.execute('''SELECT * FROM roomTbl''') # execute an SQL statment
  rv = cur.fetchall() #Retreive all rows returend by the SQL statment
  Results=[]
  for row in rv: #Format the Output Results and add to return string////////windowDir, bed,accessory,imageUrl,bookingStatus, rlevel
    Result={}
    Result['windowDir']=row[0].replace('\n',' ')
    Result['bed']=row[1]
    Result['accessory']=row[2]
    Result['imageUrl']=row[3]
    Result['bookingStatus']=row[4]
    Result['rlevel']=row[5]
    Result['roomID'] = row[6]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format


@app.route("/AvailableRooms") #Default - Show Data
def AvailableRooms(): # Name of the method
  chk_in = request.args.get('chk_in')
  chk_out = request.args.get('chk_out')
  no_of_bed = request.args.get('rooms')
  cur = mysql.connection.cursor()  #create a connection to the SQL instance
  cur.execute("SELECT * FROM roomTbl where bed="+no_of_bed+" and bookingStatus=0;") # execute an SQL statment
  rv = cur.fetchall() #Retreive all rows returend by the SQL statment
  Results=[]
  for row in rv: #Format the Output Results and add to return string////////windowDir, bed,accessory,imageUrl,bookingStatus, rlevel
    Result={}
    Result['windowDir']=row[0].replace('\n',' ')
    Result['bed']=row[1]
    Result['accessory']=row[2]
    Result['imageUrl']=row[3]
    Result['bookingStatus']=row[4]
    Result['rlevel']=row[5]
    Result['price'] = row[6]
    Result['roomID'] = row[7]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format


@app.route("/bookingEntry",methods=["POST"]) #Add Customer
def bookingEntry():
  custName = request.args.get('name')
  phone = request.args.get('phone')
  address = request.args.get('address')
  idtype = request.args.get('idtype')
  idnumber = request.args.get('idnumber')
  email = request.args.get('email')
  sex = request.args.get('sex')
  comment = request.args.get('comment')
  cur = mysql.connection.cursor() #create a connection to the SQL instance
  s='''INSERT INTO custTbl(custName,phone,address,idtype,idnumber,email,sex,comment) VALUES('{}','{}','{}','{}','{}','{}','{}','{}');'''.format(custName,phone,address,idtype,idnumber,email,sex,comment)
  cur.execute(s)
  mysql.connection.commit()

  return '{"Result":"Success"}'

@app.route("/bookingEntryV",methods=["POST"]) #Add Customer
def bookingEntryV():
  custName = request.args.get('name')
  phone = request.args.get('phone')
  address = request.args.get('address')
  idtype = request.args.get('idtype')
  idnumber = request.args.get('idnumber')
  email = request.args.get('email')
  sex = request.args.get('sex')
  comment = request.args.get('comment')
  checkin_date = request.args.get('checkin_date')
  checkout_date = request.args.get('checkout_date')
  roomID = request.args.get('roomID')
  cur = mysql.connection.cursor() #create a connection to the SQL instance
  s='''INSERT INTO custTbl(custName,phone,address,idtype,idnumber,email,sex,comment) VALUES('{}','{}','{}','{}','{}','{}','{}','{}');'''.format(custName,phone,address,idtype,idnumber,email,sex,comment)
  cur.execute(s)
  mysql.connection.commit()
  cur2 = mysql.connection.cursor()
  cur2.execute('''select MAX(custID) From custTbl''') # execute an SQL statment
  rv = cur2.fetchall() #Retreive all rows returend by the SQL statment
  Result=0
  for row in rv: #Format the Output Results and add to return string
    Result=row[0]
  cur3 = mysql.connection.cursor()
  s3='''insert into reservationTbl ( checkin_date, checkout_date, custID, roomID ) VALUES('{}','{}','{}','{}');'''.format(checkin_date, checkout_date, Result, roomID)
  cur3.execute(s3)
  mysql.connection.commit()
  
  
  response={'Results':Result}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret

@app.route("/PrintBookingDetails") #Add Customer
def PrintBookingDetails():
  custID = request.args.get('custID')
  cur4 = mysql.connection.cursor() #create a connection to the SQL instance
  cur4.execute('''select checkin_date, checkout_date, a.custID, roomID,revID ,custName,phone,address,idtype,idnumber,email from reservationTbl a,custTbl b  where a.custID={ } and b.custID={};'''.format(custID,custID) # execute an SQL statment
  rv4 = cur4.fetchall() #Retreive all rows returend by the SQL statment
  Results2=[]
  for row in rv4: #Format the Output Results and add to return string////////windowDir, bed,accessory,imageUrl,bookingStatus, rlevel
    Result2={}
    Result2['checkin_date']=row[0].replace('\n',' ')
    Result2['checkout_date]=row[1]
    Result2['custID']=row[2]
    Result2['roomID']=row[3]
    Result2['revID']=row[4]
    Result2['custName']=row[5]
    Result2['phone'] = row[6]
    Result2['address'] = row[7]
    Result2['idtype']=row[5]
    Result2['idnumber'] = row[6]
    Result2['email'] = row[7]
    Results2.append(Result2)
  response={'Results':Results2, 'count':len(Results2)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format


if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080
