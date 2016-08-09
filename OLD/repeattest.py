#This file tests fro any repeated entries in a json file and I think also deletes them

import json
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


			
	
	












