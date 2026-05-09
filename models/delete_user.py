from database.connectionMySql import Connection, mysql


def deleteUser(userId):
  try:
    cnx = Connection.connectionDB()
    cursor = cnx.cursor()
    sql = '''
        DELETE FROM persons
        WHERE id = %s;
        '''
    values = (userId,)

    cursor.execute(sql, values)
    cnx.commit()

    print(cursor.rowcount, 'Delete Registry')

    cnx.close()
  except mysql.connector.Error as error:
    print("Error to delete the registry{}".format(error))
  
