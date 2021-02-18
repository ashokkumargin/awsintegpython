import json
import os
import decimalencoder
import mysql.connector
import collections
import mysqlconnection

databaseExists = False

def list(event, context):
	db_connection = mysqlconnection.MysqlConnection().getConnection()
	
	mycursor = db_connection.cursor()
	# mycursor = db_connection.cursor(buffered=True)
	# mycursor.execute("SHOW DATABASES")

	# for x in mycursor:
		# if x[0] == 'awsmysql':	databaseExists = True
		# #print(x)
		
	# if not databaseExists: mycursor.execute("CREATE DATABASE mydatabase")
		
	mycursor.execute("SELECT * FROM user")

	myresult = mycursor.fetchall()
	
	objects_list = []
	for row in myresult:
		d = collections.OrderedDict()
		d["id"] = row[0]
		d["firstName"] = row[1]
		d["lastName"] = row[2]
		d["email"] = row[3]
		d["comments"] = row[4]
		d["options"] = row[5]
		objects_list.append(d)
	
	#print(objects_list)
    # create a response
	response = {
        "statusCode": 200,
        "body": json.dumps(objects_list, cls=decimalencoder.DecimalEncoder),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true"
        }
    }
	
	return response