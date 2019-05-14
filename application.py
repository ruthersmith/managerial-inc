'''
in anaconda terminal
$ set FLASK_APP=application.py
$ set FLASK_DEBUG=1
$ python -m flask run
'''
import helpers

from flask import Flask, session,render_template,request,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

DB_URL = "postgres://vohbopvbgbukep:8ba34e39e860c4ec52c77baa9925f8dd2c7fd64e69"
DB_URL += "a636fb35b2a94633219523@ec2-54-163-226-238.compute-1.amazonaws.com:"
DB_URL += "5432/d489mplbq8r86t"

# Set up database
engine = create_engine(DB_URL)
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    print(session)
    return render_template('loginPages/front.html')

@app.route("/login/manager")
def loginManager():
    return render_template('loginPages/manager_login.html')

@app.route("/login/tenant")
def loginTenant():
    return render_template('loginPages/tenant_login.html')

@app.route("/manager/create")
def createManager():
    return render_template('loginPages/create_manager.html')

@app.route("/manager/create",methods = ["POST"])
def managerDashboard():
    data = {}
    #check to see if we are creating a manager 
    creatingManager = int(request.form.get("createManager"))
    if creatingManager == 1:
        managerId = int(helpers.createManager(db,request))
    else:
        managerId = int(request.form.get("manager_id"))
   
    password = request.form.get("manager_pass")
    manager = helpers.authenticateManager(db,managerId,password)
    
    if(len(manager) == 0):
        return"<h1>ERROR:Failed to authenticate</h1>"
    else:
        session['manager_info'] = manager[0]
        data['manager_info'] = manager[0]
        data['tenants_info'] = helpers.getTenants(db,manager[0][0])
        return render_template('dashboards/manager_dashboard.html',data=data)
    
@app.route("/manager/addTenant",methods = ["POST"])
def addTenant():
    helpers.addTenant(db,request,session)
    return "adding tenant"

@app.route("/tenant/home",methods = ["POST"])
def tenantDashboard():
    data = {}
    
    return render_template('tenant/tenant_dashboard.html',data=data)
    





