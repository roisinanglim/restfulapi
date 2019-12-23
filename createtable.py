# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 23:28:57 2019

@author: Roisin Anglim
"""
#mport mysql.connector
import pymysql

conn = pymysql.connect(host='localhost',
                             user='root',
                             password='ROOT')
#Create database
conn.cursor().execute('create database datarepresentation CHARACTER SET utf8mb4')


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='ROOT',
                             db='datarepresentation',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

#Create a cursor 
cur = connection.cursor()

#Create a table staff
sqlQuery   = ("CREATE TABLE staff (id int AUTO_INCREMENT PRIMARY KEY, Staff_Name varchar(250),Staff_Surname varchar(250),Job_Title varchar(250),Salary int,Department varchar(250),Store_Name varchar(250))")
cur.execute(sqlQuery)


#Create a table store
sqlQuery   = ("CREATE TABLE store (id int AUTO_INCREMENT PRIMARY KEY, Store_Name varchar(250),Num_staff int)")
cur.execute(sqlQuery)


