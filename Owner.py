import datetime
import time
from typing import List

 
class Owner:
	id: int
	username: str
	creationDate: datetime
	balance: float
	#likes: List

	def __init__(self):
		self.id = 0
		self.username = ""
		self.creationDate = datetime.datetime.now()
		self.balance = 0
		#self.likes = []
	
	def __init__(self,id, username, creationDate:datetime):#, likes):
		if id==None:
			self.id = time.mktbime(datetime.datetime.now().timetuple()) * 1000
		else:
			self.id = id
		self.username = username
		self.creationDate = creationDate
		self.balance = 100
		#self.likes = likes

	def addBalance(self, amount:float):
		'''
		Adds balance when an NFT is transferd, the amount paid by the previous owner is added to the new one
		'''
		self.balance += amount

	def removeBalance(self, amount:float):
		'''
		Removes balance when an NFT is transferd, the amount paid by the new owner is removed  from him
		'''
		self.balance -= amount