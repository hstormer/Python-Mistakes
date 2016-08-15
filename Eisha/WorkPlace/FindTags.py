import pymongo
import json
from random import randint
from pymongo import MongoClient
from sys import argv
script, ofile, savefile = argv

client = MongoClient()
db = client.github
cursor = db.commits.find()


ofile = open(ofile, 'r')
savefile = open(savefile, 'w')
data = json.load(ofile)
outdata = []

done = len(data)
current = -1
counter = 0
link = ''
entry = None


for document in cursor:
	d = list(item["Tags"] for item in data)
	print d
