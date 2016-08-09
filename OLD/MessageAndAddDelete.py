import pymongo
import json
#This file adds any missing Commit Message, Additions, or/and Deletions to a json file. 

from random import randint
from pymongo import MongoClient
from sys import argv
script, ofile, savefile = argv

client = MongoClient()
db = client.github
cursor = db.commits.find()

#Cannot write to this
ofile = open(ofile, 'r')
#Will delete everything in the file
savefile = open(savefile, 'w')
data = json.load(ofile)
outdata = []

done = len(data)
current = -1
counter = 0
link = ''
entry = None
yay = ["I FOUND ONE!", "Wow, I found one!", "Yay! I found one!", "Guess what? I found one!", "I found The One!!!"]

def housecleaning(l):
	finalist = []
	list1 = []
	finish = []
	templist = []
	for line in l:
		list1.append(line)
	for i in list1:
		templist.append(i)
		if i.encode('utf8') == '\n':
			str1 = ''.join(templist)
			templist = []
			finalist.append(str1)
	str1 = ''.join(templist)
	finalist.append(str1)
	finalist.pop(0)
	list1 = []
	for i in finalist:
		list1 = []
		for line in i:
			list1.append(line)
		templist = []
		if str(list1[0])== '+' or str(list1[0]) == '-':
			str1 = ''.join(list1)
			finish.append(str1)
	return finish

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
				length = document.get("files")
				if length != [] and length != None:
					length = length[0]
					additions = length.get("additions")
					deletions = length.get("deletions")
					item["Additions:"] = additions
					item["Deletions:"] = deletions
					patch = document.get("files")
					if patch != [] and patch != None:
						patch = patch[0]
						patch = patch.get("patch")
						patch = housecleaning(patch)
						item["Changes:"] = patch
						print yay[randint(0,4)]
						outdata.append(item)
				break
	counter += 1
	#This is based on save location. If it is more than this, then change it.
	if counter == 100000:
		break

with savefile as outfile:
	json.dump(outdata, savefile, indent = 2)

	
