import mysql.connector

class   Connection:
 def connectionDB():
  
  try:
   cnx = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='12.05.16',
    database = 'users'
    )
   print('Correct Connection')
   
   return cnx

  except mysql.connector.Error as error:
   print('Error connecting to the database {}'.format(error ))

 connectionDB()