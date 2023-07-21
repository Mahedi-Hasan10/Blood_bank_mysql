import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password"
)

myCursor = mydb.cursor()

db_name = "bloodBank"
sql_command = "CREATE DATABASE "+db_name

myCursor.execute(sql_command)