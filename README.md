### Data Representation - Web Application Project 

#### Details of Repository 

This repository comprises of a web application that hosts staff and store details. The web application consumes a restful api. The restful api facilitates read, create, update and delete (CRUD) functions between the web application and the MYSQL database.


#### Website 

The website is made up of two pages. The first page contains a staff table holding the staff's details. The update, create and delete buttons within the webpage, enable the staff details to be amended. Upon clicking on any of the labelled buttons, the staff details are prompted. Once these details are submitted, the selected function is called and both the sql database and the webpage are updated. The show store button located in the centre of the page allows for easy navigation to the store table.

![StaffTable](https://github.com/roisinanglim/restfulapi/blob/master/Images/stafftablepg1.JPG)

The second page consists of the store table. This contains details about the store's locations. The update, create and delete buttons within the webpage, enable the stores details to be amended. Upon clicking on any of the labelled buttons, the store details are prompted. Once these details are submitted, the selected function is called and both the sql database and the webpage are updated. The show staff button located in the centre of the page allows for easy navigation to the staff table.

![StoreTable](https://github.com/roisinanglim/restfulapi/blob/master/Images/storetablepg2.JPG)


Both pages utilise a JavaScript contain method, to prompt the user prior to deleting information from the staff or store tables. 

![error_checking](https://github.com/roisinanglim/restfulapi/blob/master/Images/error_checking.JPG)

#### SQL Database 
The SQL database contains two tables the staff and the store tables. The employee id is identified as the primary key within the staff table and the id is the primary key within the store table. An auto_increment function is utilised on both tables, it works by automatically assigning the next id to any new staff member created.

![storesql](https://github.com/roisinanglim/restfulapi/blob/master/Images/sqlstore.JPG)
![staffsql](https://github.com/roisinanglim/restfulapi/blob/master/Images/sqlstaff.JPG)



#### Packages Required
MYSQL - You will require an SQL database to create and store the tables details. [Download Here ](https://www.mysql.com/downloads/)

Python - You will require python to generate your functions to conduct the CRUD commands. [Download Here](https://www.anaconda.com/distribution/)

Flask Server - This will be required to interact and return information between the browser and the database. This is not download as part of the anaconda package. To install flask run the following command in the command prompt  - pip install flask.


Virtual Environment - Create virtual environment run python-m venv venv in the command prompt. Run pip freeze > requirements.txt to save all of the packages.


#### How to run the repository 
 1. Download the repository folder.
 2. Through the command navigate to the folder 
 3. In the command prompt activate the virtual environment running the commend - python-m venv venv
 4. Set FLASK_APP=server1
 5. Run the flask server using the command - flask run
 6. Go to the URL - http://127.0.0.1:5000/staffcrud.html
