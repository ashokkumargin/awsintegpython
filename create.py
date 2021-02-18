import json
import os
import time
import uuid
import mysqlconnection

def create(event, context):
	data = json.loads(event['body'])
	
	timestamp = int(time.time() * 1000)
	
	db_connection = mysqlconnection.MysqlConnection().getConnection()
	mycursor = db_connection.cursor()
	
	sql = "INSERT INTO user (id, firstName,lastName,email,comments,options,checked,createdAt,updatedAt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = (str(uuid.uuid1()), data['firstName'], data['lastName'], data['email'], data['comments'], data['options'], str('False'), str(timestamp), str(timestamp))
	
	mycursor.execute(sql, val)

	db_connection.commit()

	print(mycursor.rowcount, "record inserted.")	
    
    ## Items to populate the table
	item = {
        'id': str(uuid.uuid1()),
        'firstName': data['firstName'],
        'lastName': data['lastName'],
        'email': data['email'],
        'comments': data['comments'],
        'options': data['options'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp
    }

    # create a response
	response = {
        "statusCode": 200,
        "body": json.dumps(item),
        "headers": {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true"
        }
    }

	return response