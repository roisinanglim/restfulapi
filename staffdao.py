# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 21:04:42 2019

@author: Harvey Norman
"""
#Create connection to mySql
import pymysql

#Create a class to contain functions
class staffsdao:
    #Create variable db
    db=""
    def __init__(self):
        #Set the database and add login information
        self.db = pymysql.connect(host='localhost',
                             user='root',
                             password='ROOT',
                             db='datarepresentation',
                             charset='utf8mb4',
                             )
    
    def create(self,values):
       #Get the dtatbase from the class created
        cursor = self.db.cursor()
        #Adds vales passed into the function and updates the staff table created within the database
        sql = "insert into staff (Staff_Name,Staff_Surname,Job_Title,Salary,Department,Store_Name) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,values)
        
        self.db.commit()
        return cursor.lastrowid
    
    def create_store(self,values):
        cursor = self.db.cursor()
        sql = "insert into store (Store_Name,Num_staff) values (%s,%s)"
        cursor.execute(sql,values)
        self.db.commit()
        return cursor.lastrowid
    
    
    def getAll(self):
        #Get the dtatbase from the class created
        cursor = self.db.cursor()
        sql="select * from staff"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray
    
    def getAll_store(self):
        #Get the dtatbase from the class created
        cursor = self.db.cursor()
        sql="select * from store"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary_store(result))

        return returnArray 
    
    
    def findById(self,id):
        cursor = self.db.cursor()
        sql = "select * from staff where id = %s"
        values = (id,)
        
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)
    #self.convertToDictionary(result)
    
    def findById_store(self,id):
        cursor = self.db.cursor()
        sql = "select * from store where id = %s"
        values = (id,)
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDictionary_store(result)
    
    def update(self,values):
        cursor = self.db.cursor()
        sql = ("update staff set Staff_Name = %s,Staff_Surname = %s, Job_Title =%s , Salary = %s ,Department = %s, Store_Name = %s where id = %s")
        cursor.execute(sql,values)
        self.db.commit()
        
    def update_store(self,values):
        cursor = self.db.cursor()
        sql = ("update store set Store_Name = %s,Num_staff = %s where id = %s")
        cursor.execute(sql,values)
        self.db.commit()     
    
    def delete(self,id):
        cursor = self.db.cursor()
        sql = "delete from staff where id = %s"
        values = (id,)
        
        cursor.execute(sql,values)
        self.db.commit()
        print("delete done")
        
    def delete_store(self,id):
        cursor = self.db.cursor()
        sql = "delete from store where id = %s"
        values = (id,)
        cursor.execute(sql,values)
        self.db.commit()
        print("delete done")     
        
    def convertToDictionary(self, result):
        colnames = ["id","Staff_Name","Staff_Surname","Job_Title","Salary","Department","Store_Name"]
        item = {}
        
        if result:
            for i, colnames in enumerate(colnames):
                value = result[i]
                item[colnames] = value
        return item
    
    def convertToDictionary_store(self, result):
        colnames = ["id","Store_Name","Num_staff"]
        item = {}
        
        if result:
            for i, colnames in enumerate(colnames):
                value = result[i]
                item[colnames] = value
        return item
staffdao = staffsdao()   
        
        