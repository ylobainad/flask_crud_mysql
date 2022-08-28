# flask_crud_mysql
https://www.youtube.com/watch?v=BP3D03CYFHA   ----> Flask SQLAlchemy CRUD con MySQL

Install MySQL in ubuntu 20.04(https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

Step 1 — Installing MySQL
1- sudo apt update
2- sudo apt install mysql-server
3- sudo systemctl start mysql.service

Step 2 — Configuring MySQL
1- sudo mysql
2- ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
3- exit

Step3 - Login
1- mysql -u root -p

Creata a databse:
CREATE DATABASE name_database;

Show databases:
SHOW DATABASES;

Show tables:
1- use contactsdb;
2- show tables; 
3- select * from contact;



Install SQLAlchemy(https://pypi.org/project/SQLAlchemy/)
pip install SQLAlchemy(doesn't work with VSCode, instead with pipenv works ok)

pipenv install Flask-SQLAlchemy

##########################################################################################
Install client mysql for Python using pipenv:

###install mysql client lib for the OS###
1- sudo apt install libmysqlclient-dev

2- pipenv install mysqlclient





