
import mysql.connector

class ConexionDataBase:
    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd




conexion = mysql.connector.connect(host="localhost", user= "root", passwd = "", database = "mybankdb")
print(conexion)
cursor = conexion.cursor()




#cursor.execute()