import datetime
from turtle import update
import Owner
import time
import persistance 
class NFT:
	id: int
	name:str
	description:str
	creationDate: datetime
	owner: Owner
	price:float

	def __init__(self):
		self.id = 0
		self.name = ""
		self.description = ""
		self.creationDate = datetime.datetime.now()
		self.owner = Owner()
	
	def __init__(self, id, name, description, creationDate:datetime, owner, price):
		self.name = name
		self.description = description
		self.creationDate = creationDate
		if id==None:
			self.id = time.mktime(datetime.datetime.now().timetuple()) * 1000
		else:
			self.id = id
		self.owner = owner
		self.price = price

	def transfer(self, old_owner: Owner, newOwner:Owner, price=None)-> bool:
		'''
		Transfer the NFT from the current owner to the new owner with the set price.
		Uses the NFT price if no specific price is set.

		Set the price to 0 to transfer the NFT for free.

		Returns true if the transfer was successful, false otherwise
		'''
		if price==None:
			price = self.price
		if newOwner.balance >= price:
			
			old_owner.addBalance(price)
			newOwner.removeBalance(price)
			self.owner = newOwner #transfer the nft ownership
			return persistance.updateNFT(self, old_owner)
			
			return True
		
		return False


