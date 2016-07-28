import json

ofile = raw_input("What file would you like to add additions and deletions to?  ")
ofile = open(ofile, 'a+')

data = json.load(ofile)

for i in data:
	if i.get("Changes:") != None:
		#Does have changes
		changes = i.get("Changes:")
		additions = 0
		deletions = 0
		for change in changes:
			if str(change[0]) == '+':
				additions += 1
			elif str(change[0]) == '-':
				deletions += 1
		i["Additions:"] = additions
		i["Deletions:"] = deletions
		print i
	else:
		#Did not have recorded changes, skip it
		pass

ofile.seek(0)
ofile.truncate()
with ofile as outfile:
	json.dump(data, outfile, indent = 2)

	
