#this program goes through the yes.json or no.json file to check for any repeats

from sys import argv
import json
#import finalyes.json
from pymongo import MongoClient
script, open_file = argv
client = MongoClient()
db = client.github

with open('Hello.json') as f:
	entries = json.load(f)
first_list = []
new_list = []
x = entries.pop()
new_list.append(x)


for i in entries:
	link = i.get('Commit Corrections')
	#print link
	first_list.append(i)
	for k in new_list:
		#print k.get('Commit Corrections')
		if link in k.get('Commit Corrections'):
			print "We found a duplicate"
			print k.get('Commit Corrections')
			break
		else:
			new_list.append(i)
			break
print first_list
print new_list
print len(first_list)
print len(new_list)

#f = open(finalyes.json, 'r+') 
#text = f.read()
#f.write(

			
	
	












