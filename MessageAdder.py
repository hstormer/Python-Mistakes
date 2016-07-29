import pymongo
import json
from random import randint
from pymongo import MongoClient

client = MongoClient()
db = client.github
cursor = db.commits.find()

ofile = raw_input("What file would you like to add commit messages to?")
ofile = open(ofile, 'a+')
data = json.load(ofile)

done = len(data)
current = -1
counter = 0
link = ''
entry = None
yay = ["I FOUND ONE!", "Wow, I found one!", "Yay! I found one!", "Guess what? I found one!"]

for document in cursor:
	lonk = document.get("html_url")
	d = list(item["Commit Corrections"] for item in data)
	if lonk in d:
		for item in data:
			if str(item.get("Commit Corrections")) == str(lonk): 
				message = document.get("commit")
				message = message.get("message")
				link = data[current].get("Commit Corrections")
				item["Message:"] = message
				print yay[randint(0,3)]
				break
	counter += 1
	#This is based on save location. If it is more than this, then change it.
	if counter == 100000:
		break

ofile.seek(0)
ofile.truncate()
with ofile as outfile:
	json.dump(data, outfile, indent = 2)

	
