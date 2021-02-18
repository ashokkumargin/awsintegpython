import mysql.connector

class MysqlConnection(object):
	
	#def __init__(self):
		#self._con = MysqlConnection.getConnection()
		#self._cursor = self._con.cursor()
		
	@staticmethod
	def getConnection():
		db_connection = mysql.connector.connect(
		  host="awsmysql-1.c66v1kaibbzi.us-east-1.rds.amazonaws.com",
		  port="3001",
		  user="awsmysql",
		  passwd="awsmysql",
		  database="awsmysql"
		)
		return db_connection
