#from sqlite3 import Cursor
import sqlite3
import string
from typing import List

from numpy import integer
from NFT import *
from Owner import *
from sqlite3 import Error
import mysql.connector



def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            user=user_name,
            passwd=user_password,
			host=host_name,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("localhost", "root", "mysql","Mighty_Market")


#select *

def selectNFT()->List:

	cursor = connection.cursor()
	'''
		Returns the NFTs from DB
	'''
	query = cursor.execute("SELECT * FROM NFT")
	if type(query) == None:
		return 'The list is empty'
	else:
		fetch = cursor.fetchall()
		
		return fetch

def selectOwn()-> List:
	cursor = connection.cursor()
	query = cursor.execute("SELECT * FROM Owner")
	if type(query) == None:
		return 'The list is empty'
	else:
		fetch = cursor.fetchall() 
		return fetch
	
def selectLikes(n1) -> int:
	'''
	The function gives the amount of likes in an NFT
	'''
	cursor = connection.cursor()
	id = n1['id']
	id = str(id)
	cursor.execute("Select LENGTH(IDLIKE) from Likes where IDNFT = "+id) 
	if type(cursor) == None:
		return 'The list is empty'
	else:
		fetch = cursor.fetchall()
		return fetch

# mint 

def insert(n1):

	'''
	Insers NFT on database 
	'''
	cursor = connection.cursor()
	try:
		sql = "INSERT INTO NFT (id, name, description, creation_date, owner, price) VALUES (%s, %s, %s, %s, %s, %s)"
		val = (n1.id, n1.name, n1.description, n1.creationDate, 934, n1.price)
		cursor.execute(sql, val)

		res = connection.commit()  #ver como llamo a la base de datos
		
		return 'Commit succesfully done'

	except Exception as e:
		return e.__str__()
		return 'An error occurred while comminting'
	
#transfer

def updateNFT(n1, u1):
	''' 
	Updates price and owner on NFT in database
	'''
	cursor = connection.cursor()
	cursor2= connection.cursor()
	cursor3 = connection.cursor()
	try:
		
		sql="UPDATE NFT SET owner = %s, price = %s WHERE id = %s;"
		variables = (n1.owner.id, n1.price, n1.id)
		cursor.execute(sql, variables)

		

		sql2 = "UPDATE Owner SET balance = %s WHERE id = %s;"
		var2 = (n1.owner.balance, n1.owner.id)
		cursor2.execute(sql2, var2)

		var3= (u1.balance, u1.id)
		cursor3.execute(sql2, var3)

		res = connection.commit()


		return True
	
	except Exception as e:
		return e.__str__()
