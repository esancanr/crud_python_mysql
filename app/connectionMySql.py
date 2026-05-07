import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class   Connection:
 def connectionDB():
  
  try:
   cnx = mysql.connector.connect(
    host=os.getenv("HOST_DB"),
    port=os.environ.get("PORT_DB"),
    user=os.environ.get("USER_DB"),
    password=os.environ.get("PASSWORD_DB"),
    database =os.environ.get("DATABASE_DB")
    )
   print('Correct Connection')
   
   return cnx

  except mysql.connector.Error as error:
   print('Error connecting to the database {}'.format(error ))

 connectionDB()