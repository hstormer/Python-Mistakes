import pymongo
from pymongo import MongoClient
client = MongoClient('10.13.10.124')
db = client.github
cursor = db.commit_comments.find()
message = ''
things = ["indentation", "typo", "tyro", "bracket", "misspell", "mistake", "syntax"]

for document in cursor:
	message = document.get("body")
	link = document.get("html_url")
	for i in things:
		if i in message:
			print message
			print link
			print "============================================"


