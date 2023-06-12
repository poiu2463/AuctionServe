import mysql.connector

'''
This class should provide methods for getting info from the database. 
It should pull the database connection values from the settings config file.
'''

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb)