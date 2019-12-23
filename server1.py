# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:37:42 2019

@author: Harvey Norman
"""
from flask import Flask,jsonify,request,abort
from staffdao import staffdao

#Create database
#conn.cursor().execute('create database datarepresentation CHARACTER SET utf8mb4')


#make_reponse
#from flask_cors import CORS

#Creates a server 
app = Flask(__name__,static_url_path='',static_folder='.')



#"Department":"Finance","Job_Title":"Senior Accountant","Salary":40000,"Staff_Name":"Roisin","Staff_Surname":"Anglim","id":12345}

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Department\":\"IT\",\"Job_Title\":\"Manager\",\"Salary\":45000,\"Staff_Name\":\"George\",\"Staff_Surname\":\"Gore\",}" http://127.0.0.1.5000/staff

# Create function to return all staff information
@app.route('/staff')
def getAll():
    results = staffdao.getAll()
    return jsonify(results)

# Create function to return all staff information
@app.route('/store')
def getAll_store():
    results = staffdao.getAll_store()
    return jsonify(results)

# Create function to return all staff detail by employee id
@app.route('/staff/<int:id>')
def findById(id):
    foundstaff =staffdao.findById(id)
    #if len(foundstaff) == 0:
     #   return jsonify ({}), 204
    return jsonify(foundstaff)

# Create function to return all store detail by store id
@app.route('/store/<int:id>')
def findById_store(id):
    foundstore = staffdao.findById_store(id)
    return jsonify(foundstore)

#Add addtional staff detail
@app.route('/staff',methods=['POST'])
def create():
    if not request.json:
        abort(400)
    staffs = {"Staff_Name":request.json['Staff_Name'],
                 "Staff_Surname":request.json['Staff_Surname'],
                  "Job_Title":request.json['Job_Title'],
                 "Salary":request.json['Salary'],
                 "Department":request.json['Department'],
                 "Store_Name":request.json['Store_Name']}
    
    values = (staffs['Staff_Name'],staffs['Staff_Surname'],staffs['Job_Title'],staffs['Salary'],staffs['Department'],staffs['Store_Name'])
    newId = staffdao.create(values)
    staffs['id'] = int(newId)
    return jsonify(staffs)    
    
    
#Add addtional store detail
@app.route('/store',methods=['POST'])
def create_store():
    #global nextid
    if not request.json:
        abort(400)
    stores = {"Store_Name":request.json['Store_Name'],
                 "Num_staff":request.json['Num_staff']}
    values = (stores['Store_Name'],stores['Num_staff'])
    newId = staffdao.create_store(values)
    stores['id'] = int(newId)
    return jsonify(stores)    

#Update staff detail
@app.route('/staff/<int:id>',methods=['PUT'])
def update(id):
    foundstaff = staffdao.findById(id)
    if not foundstaff:
        abort(404)
    if not request.json:
        #To report that it didnt work
        abort(400)
    reqJson = request.json
    if 'Salary' in reqJson and type(reqJson['Salary']) is not int:
        abort(400)
        
    if "Staff_Name" in reqJson:
        foundstaff["Staff_Name"] = reqJson["Staff_Name"]
    if "Staff_Surname" in reqJson:
        foundstaff["Staff_Surname"] = reqJson["Staff_Surname"]
    if "Salary" in reqJson:
        foundstaff["Salary"] = reqJson["Salary"]
    if "Job_Title" in reqJson:
        foundstaff["Job_Title"] = reqJson["Job_Title"]
    if "Department" in reqJson:
        foundstaff["Department"] = reqJson["Department"]
    if "Store_Name" in reqJson:
        foundstaff["Store_Name"] = reqJson["Store_Name"]     
    
    values = (foundstaff['Staff_Name'],foundstaff['Staff_Surname'],foundstaff['Job_Title'],foundstaff['Salary'],foundstaff['Department'],foundstaff['Store_Name'],foundstaff['id'])
    staffdao.update(values)
    return jsonify(foundstaff) 

#Update staff detail
@app.route('/store/<int:id>',methods=['PUT'])
def update_store(id):
    foundstore = staffdao.findById_store(id)
    if not foundstore:
        abort(404)
    if not request.json:
        #To report that it didnt work
        abort(400)
    reqJson = request.json
    if 'Num_staff' in reqJson and type(reqJson['Num_staff']) is not int:
        abort(400)
        
    if "Store_Name" in reqJson:
        foundstore["Store_Name"] = reqJson["Store_Name"]
    if "Num_staff" in reqJson:
        foundstore["Num_staff"] = reqJson["Num_staff"]
    
    values = (foundstore['Store_Name'],foundstore['Num_staff'],foundstore['id'])
    staffdao.update_store(values)
    return jsonify(foundstore)           

#Delete staff detail
@app.route('/staff/<int:id>',methods=['DELETE'])
def delete(id):
    staffdao.delete(id)
    return jsonify ({"done":True})

#Delete staff detail
@app.route('/store/<int:id>',methods=['DELETE'])
def delete_store(id):
    staffdao.delete_store(id)
    return jsonify ({"done":True})

if __name__ == '__main__' :
     app.run(debug= True)