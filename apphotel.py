from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask_cors import CORS
import json
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

@app.route("/addCustomer") #Add Customer
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
if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080
