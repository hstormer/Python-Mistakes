import pymongo
from pymongo import MongoClient
client = MongoClient('10.13.10.124')
db = client.github
cursor = db.commit_comments.find()
message = ''
things = ["indentation", "typo", "tyro", "fixed", "bracket", "misspell", "mistake", "syntax"]

for document in cursor:
	message = document.get("body")
	for i in things:
		if i in message:
			print message
			print "============================================"


