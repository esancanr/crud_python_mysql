from database.connectionMySql import *

class Users:
 def createUsers(name, lastname, gender):
  try:
    cnx = Connection.connectionDB()
    cursor = cnx.cursor()

    sql ='INSERT INTO persons values(null,%s,%s,%s);'
    values = (name, lastname, gender)

    cursor.execute(sql, values)
    cnx.commit()

    print(cursor.rowcount, 'New Regestry')

    cursor.close()
    cnx.close()
  except mysql.connector.Error as error:
    print("Error {}".format(error))
  
