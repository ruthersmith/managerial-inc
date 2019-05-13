# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:28:31 2019

@author: bercy
created for the landlord/tenant application
"""

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
    return rows[0]

def authenticateManager(db,managerId,password):
    rows = []
    sql = "SELECT * FROM buildingManager WHERE managerid = :managerId and "
    sql += "password = :password"
    result =  db.execute(sql,{"managerId":managerId, "password":password})
    
    for row in result:
        rows.append(row)
    
    return rows
    
    
    
    
    