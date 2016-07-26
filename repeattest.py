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
		lonk = k.get('Commit Corrections')
		if link in lonk:
			print "We found a duplicate"
			print k.get('Commit Corrections')
			break
		elif lonk in link:
			print "We found a duplicate"
			print k.get('Commit Corrections')
			new_list.remove(k)
			break
		else:
			new_list.append(i)
			print "Adding to the list"
			break

print len(first_list) + 1  #all entries
print len(new_list) # entries without duplicates
print first_list
print new_list
print len(first_list) + 1
print len(new_list)

#f = open(finalyes.json, 'r+') 
#text = f.read()
#f.write(
=======

ofile = raw_input("What file do you want to check for duplicates?")

ofile = open(ofile, 'a+')
entries = json.load(ofile)

nlist = []
nlist.append(entries[0])
link = None
duplicates = 0

for entry in entries:
	link = entry.get('Commit Corrections')
	counter = 0
	for item in nlist:
		link2 = item.get('Commit Corrections')
		if link in link2:
			print "We found a duplicate!"
			duplicates += 1
			counter = 0
			print link
			print link2
			break
		else:
			counter += 1
	if counter == len(nlist):
		nlist.append(entry)

duplicates -= 1
print "We found %d duplicates." % duplicates

ofile.seek(0)
ofile.truncate()
with ofile as outfile:
	json.dump(nlist, outfile, indent = 2)


			
	
	












