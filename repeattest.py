#this program goes through the yes.json or no.json file to check for any repeats

from sys import argv
import json
#import finalyes.json
from pymongo import MongoClient
script, open_file = argv
client = MongoClient()
db = client.github

with open('temp.json') as f:
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
			new_list.remove(k)
			break
		else:
			new_list.append(i)
			break

print len(first_list) + 1  #all entries
print len(new_list) # entries without duplicates

#f = open(finalyes.json, 'r+') 
#text = f.read()
#f.write(

			
	
	












