from database.connectionMySql import Connection, mysql


def modifyUser(userId ,name, lastName, gender):
  try:
    cnx = Connection.connectionDB()
    cursor = cnx.cursor()
    sql = """
        UPDATE persons
        SET userName=%s, lastName=%s, Gender=%s
        WHERE id=%s
        """
    values = (name, lastName, gender, userId)

    cursor.execute(sql, values)
    cnx.commit()

    print(cursor.rowcount, 'Update Registry')

    cnx.close()
  except mysql.connector.Error as error:
    print("Error {}".format(error))
  
