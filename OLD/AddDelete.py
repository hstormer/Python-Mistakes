import json
import pymongo
from random import randint
from pymongo import MongoClient

client = MongoClient()
db = client.github
cursor = db.commits.find()

ofile = raw_input("What file would you like to add addtions, deletions, and length to? ")
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
	link = data[counter].get("Commit Corrections")
	if str(lonk) == str(link):
		length = document.get("files")
		if length != [] and length != None:
			length = length[0]
			additions = length.get("additions")
			deletions = length.get("deletions")
		data[counter]["Additions:"] = additions
		data[counter]["Deletions:"] = deletions
		print yay[randint(0,3)]
		if data[counter].get("Length"):
			counter += 1
		#This is based on save location. If it is more than this, then change it.
		if counter == 100000:
			break

ofile.seek(0)
ofile.truncate()
with ofile as outfile:
	json.dump(data, outfile, indent = 2)

	
