from sys import argv
import json

item = None

# Run the program with the name of the file to open after the script name (in this case test.txt)
file1 = raw_input("Which file do you want to read?: ")

with open(file1) as data_file:
	data = json.load(data_file)

store = None

for i in data:
	if i.get("Additions") != None:
		store = i.get("Additions")
		i.pop("Additions")
		i["Additions:"] = store
		print "Changed one Additions to Additions:"

for i in data:
	if i.get("Deletions") != None:
		store = i.get("Deletions")
		i.pop("Deletions")
		i["Deletions:"] = store
		print "Changed one Deletions to Deletions:"

for i in data:
	if i.get("Changes") != None:
		store = i.get("Changes")
		i.pop("Changes")
		i["Changes:"] = store
		print "Changed one Changes to Changes:"

for i in data:
	if i.get("Length") != None:
		store = i.get("Length")
		i.pop("Length")
		i["Length:"] = store
		print "Changed one Length to Length:"

for i in data:
	if i.get("Commit Corrections") != None:
		store = i.get("Commit Corrections")
		i.pop("Commit Corrections")
		i["Commit Corrections:"] = store
		print "Changed one Commit Corrections to Commit Corrections:"


for i in data:
	if i.get("Commit Mistakes") != None:
		store = i.get("Commit Mistakes")
		i.pop("Commit Mistakes")
		i["Commit Mistakes:"] = store
		print "Changed one Commit Mistakes to Commit Mistakes:"

for i in data:
	if i.get("Commit Mistake") != None:
		store = i.get("Commit Mistake")
		i.pop("Commit Mistake")
		i["Commit Mistakes:"] = store
		print "Changed one Commit Mistake to Commit Mistakes:"

for i in data:
	if i.get("Tags") != None:
		store = i.get("Tags")
		i.pop("Tags")
		i["Tags:"] = store
		print "Changed one Tags to Tags:"

for i in data:
	if i.get("Mistakes") != None:
		store = i.get("Mistakes")
		i.pop("Mistakes")
		i["Mistakes:"] = store
		print "Changed one Mistakes to Mistakes:"

for i in data:
	if i.get("Mistake") != None:
		store = i.get("Mistake")
		i.pop("Mistake")
		i["Mistakes:"] = store
		print "Changed one Mistake to Mistakes:"

for i in data:
	if i.get("Why Not") != None:
		store = i.get("Why Not")
		i.pop("Why Not")
		i["Why Not:"] = store
		print "Changed one Why Not to Why Not:"

for i in data:
	if i.get("Keyword:") != None:
			del i["Keyword:"]


for i in data:
	if i.get("Mistakes:") != None:
			del i["Mistakes:"]

for i in data:
	if i.get("Mistake:") != None:
			del i["Mistake:"]

for i in data:
	if i.get("Why Not:") != None:
			del i["Why Not:"]
for i in data:
	if i.get("Length:") != None:
			del i["Length:"]


for i in data:
	print i
	assert "Additions:" in i
	assert "Deletions:" in i
	assert "Changes:" in i
	assert "Commit Mistakes:" in i
	assert "Commit Corrections:" in i
	assert "Tags:" in i
	assert "Message:" in i
	assert "Why Not:" not in i
	assert "Mistakes:" not in i
	assert "Length:" not in i
	assert len(i) == 7


print data[0]
item = data[0]
print len(data)
print item
print item.get("Commit Mistakes")


file1 = open(file1, 'w')
with file1 as outfile:
	json.dump(data, outfile, indent = 2)

	
