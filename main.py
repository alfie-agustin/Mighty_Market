from NFT import *
from Owner import *
from flask import Flask
from flask import request,make_response
from persistance import insert, selectLikes, selectNFT, selectOwn
import requests as requests
import dateutil.parser as parser

 

NFTs = [] 
Owners =[]
fetch2 =  selectOwn()
fetch = selectNFT()


for i in fetch:
	NFTs.append(NFT(i[0],i[1], i[2], i[3], i[4], i[5]))


for i in fetch2:
	Owners.append(Owner(i[0],i[1], i[2]))


app = Flask(__name__)



@app.route('/transfer', methods = ["POST"])
def transfer():
	req = request.json 
	nft = "" 
	newOwnerId = "" 
	price = None

	''' checks parameteres'''
	if "nft" in req and "newOwner" in req:
		nft = req["nft"]
		newOwnerId = req["newOwner"]
		if "price" in req:
			price = req["price"]
	else:
		return make_response("Missing parameters", 400) #create error and return it

	'''looks for NFT and transfers it'''

	for i in NFTs: 
		if i.id == nft:
			for owner in Owners:
				if owner.id == newOwnerId:
					for old_owner in Owners:
						print(Owners[0])
						if i.owner == old_owner.id:
							if i.transfer(old_owner, owner, price):
								return "NFT transferred"
							else:
								return "Error transferring NFT"
			return "New owner not found"
		


@app.route('/mint', methods = ["POST"])
def mint():

	req = request.json
	print(request)
	if req is not None:
		print(NFTs[0])
		if any(nft for nft in NFTs if nft.id == req['id']): 
			return make_response("ID already used", 400) #create error and return it
		else:
			if "id" in req and "name" in req and "description" in req and "creationDate" in req and "owner" in req and "price" in req :
				n1 = NFT(req['id'], req['name'], req['description'], parser.parse(req['creationDate'],dayfirst = True), req['owner'], req['price']) 
				insert(n1)
				return 'NFT minted'
			else:
				return make_response("Missing parameters",400)


@app.route('/Likes', methods = ["GET"])
def likes():
	
	req = request.json
	if "id" in req:
		idnft = req['id']
		for nft in NFTs: 
			if nft.id == idnft:
				cant = selectLikes(req)[0][0]
				cant = str(cant)
				return "The NFT has "+cant+" likes"
	else:
		return make_response("Missing parameters", 400)

	


if __name__ == "__main__":

	app.run()