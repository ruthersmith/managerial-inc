# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:28:31 2019

@author: bercy
created for the landlord/tenant application
"""
testGetTenant = False
testCreateManager = False

def createManager(db,request):
    firstName = request.form.get("manager_fname")
    lastName = request.form.get("manager_lname")
    phoneNum = request.form.get("manager_phone")
    email = request.form.get("manager_email")
    password = request.form.get("manager_pass")
    
    sql = "Insert Into buildingManager(firstName,lastName,phoneNum,email,password)" 
    sql += "Values(:firstName,:lastName,:phoneNum,:email,:password)"
    db.execute(sql,{"firstName":firstName,"lastName":lastName,
                    "phoneNum":phoneNum,"email":email,"password":password})
    db.commit()
    
    #get the manager id of the newly created manager
        #where we store the result of the query
    rows =  []
    sql = "SELECT managerid FROM buildingManager where "
    sql += "firstName = :firstName and password = :password"
    result =  db.execute(sql,{"firstName":firstName, "password":password})
    for row in result:
        rows.append(row)
    
    if(testCreateManager):
        print(rows[0][0])
        print(rows)
        
    return rows[0][0]

def authenticateManager(db,managerId,password):
    rows = []
    sql = "SELECT * FROM buildingManager WHERE managerid = :managerId and "
    sql += "password = :password"
    result =  db.execute(sql,{"managerId":managerId, "password":password})
    
    for row in result:
        rows.append(row)
    
    return rows

def addTenant(db,request,session):
    password	= request.form.get("tenant_pass")	
    firstname	= request.form.get("tenant_fname").capitalize()	
    lastname  = request.form.get("tenant_lname").capitalize()		
    roomnumber = int(request.form.get("tenant_room"))	
    #we have to get manager id  from session
    managerid = int(session['manager_info'][0])
    username	= request.form.get("tenant_uname")	
    
    
    sql = "INSERT INTO tenants(password,firstname,lastname,roomnumber,managerid,username)"
    sql +=" VALUES(:password,:firstname,:lastname,:roomnumber,:managerid,:username)"
    
    db.execute(sql,
               {"password":password,"firstname":firstname,"lastname":lastname,
                "roomnumber":roomnumber,"managerid":managerid,"username":username})
    db.commit()
    
def getTenants(db,managerid):
    rows = []
    sql = "SELECT * FROM tenants where managerid = :managerid"
    result = db.execute(sql,{"managerid":int(managerid)})
    for row in result:
        rows.append(row)
    
    if(testGetTenant):   
        print("getting rows")
        print(rows)
        print(managerid)
    return rows

def messageTenants(db,request,tenantid):
    notification = request.form.get("notification")
    
    sql = "INSERT INTO NotificationToTenant(notification,tenantid ) "
    sql += "VALUES(:notification,:tenantid)"
    db.execute(sql,{"notification":notification,"tenantid":tenantid})
    db.commit()
    
def getTenantMsg(db,tenantid):
    rows = []
    sql = "SELECT notification FROM NotificationToTenant where tenantid is Null "
    sql += "or tenantid = :tenantid"
    result = db.execute(sql,{"tenantid":tenantid})
    
    for row in result:
        rows.append(row)
    
    print(rows)
    return rows

def authenticateTenant(db,request):
    rows = []
    username = request.form.get("tenant_username")
    password = request.form.get("tenant_pass")
    sql = "SELECT * FROM tenants where username = :username and password = :password"
    result = db.execute(sql,{"username":username,"password":password})
    for row in result:
        rows.append(row)
    
    return rows
    
    
        
    
    
    
    