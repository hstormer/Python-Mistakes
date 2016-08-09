#modifies any entries in a json file (e.g if you wanna add colons to "Mistake" to make it "Mistake:")

import json

ofile = raw_input("Which file do you want to modify? ")
ofile = open(ofile, 'a+')


entries = json.load(ofile)

print "Here is a sample entry:"
print entries[0]
mod = raw_input("Which key would you like to modify? " )
entry = entries[0]
print "Key to be modified is %s" % mod
rep = raw_input("What would you like to replace the key %s with? " % mod)
print "Replacing key %s with %s..." %(mod, rep)

store = None
modentries = []

for entry in entries:
	store = entry.get(mod, None)
	print store
	if store != None:
		entry.pop(mod)
		entry[rep] = store
		print entry.get(rep)
	else:
		print "Key is already equal to %s." % rep
	modentries.append(entry)

ofile.seek(0)
ofile.truncate()
with ofile as outfile:
	json.dump(modentries, outfile, indent = 2)

print "All done!"
	
