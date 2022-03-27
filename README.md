---
description: >-
  Development of a restful API for a Opensea clone with limited functionalites
  (mint and transfer NFTs and knowledge of their likes.
---

# Mighty Market

## Restful API

### Libraries

For the development of the API the following Libraries were used.\
Flask: This library helped to easily render the web page and create the endpoints.\
Mysql-conector: This one  was used in order to communicate with the data base. Helped the establish the connection, to absorb information with the select querys and insert and update the database with new information.\
sqlite3: Used for running the different errors.\
datetime: Used in the classes NFT and owner. The library was used for the datatype in the creationdate attributes, but is also used for creating the id, that are composed from the time (to the thousandth).\
requests:

### Objects

The objects used for the creation of the API are NFT and Users.\
The NFT object has 6 attributes; id, name, description, creationDate, owner and price. \
The Owner object has 5 attributes; id, username, creationDate, balance and likes.

### Persistance:

The persistance file has an important role in the program because is the one who interacts with the db. This file (???????) not only creates the connection with the data base but also helps to communicate with it; From select querys (that absorbs the data from the db), to update and insert new data into the db.

### Endpoints

There are 3 endpoints in the API  and their functions are in the main.\
The first endpoint is called transfer and is used when theres a sell of an NFT. This function gets the information from the request, such as the nft and the new owner of the NFT.  The first conditional part of the function  of the function checks if all the parameters were given by the consumer. The second part of the function looks for the nft in the db and also looks for the owner, for later changing the owner data in the NFT and the balances of the users, both in the db.\
The second endpoint  is called mint, and is used when a consumer wants to mint an NFT. After the data was absorbed with the requests library, the function checks if the id of the NFT is already used, if the ID is new, the following step is to check if all the parameters were given, and if every one of them is correct, the NFT proceeds to be inserted in the data base.\
The third endpoint aims to get the likes amount of an NFT. This function checks if the nfts is in the database, and if is in there, the program will give the amount of likes that this NFT has.D

## Data base

MySQL is a relational database management system based on SQL.&#x20;

The data based has 3 tables; NFT, Owners and Likes. The NFT table has 6 attributes and the information of all the NFTs; ID (primary key) , Name, Description, Creationdate, Owner(Foreign key), price. The owners table has 4 attributes and has the information of the users; ID (primary key), Username, Creation_date, balance. The last table is called Likes, this one is a pivot table that helps to track the likes amount of the NFTs; the attributes in the table are, ID\_like (primary key), IDOwner (Foreign key) and IDNFT (foreign key)._

### Illustrative image of the data base model![](<.gitbook/assets/WhatsApp Image 2022-03-27 at 3.38.38 AM.jpeg>)



## Testing?
