from database.connectionMySql import Connection, mysql

def showUsers():
  try:
    cnx = Connection.connectionDB()
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM persons;')
    result = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return result
  except mysql.connector.Error as error:
    print("Error to show data {}".format(error))
