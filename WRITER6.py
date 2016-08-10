#Use this writer to combine all letter attributes into one and also to look at the actual python changes being made as well as the number of characters changed.

import json
import codecs
from sys import argv
script, arff_file = argv
import unicodedata

answer = raw_input("\nWARNING: \nTHIS WILL OVERWRITE THE %s FILE! \nPress any key to continue..." % arff_file)
txt2 = open(arff_file, 'w')
text = ''
print "\n%s file cleared..." % arff_file


# Add the attributes so it is ready for the data to be entered.
attributes = ["\n@relation python_mistakes", "\n", "\n@attribute commit_message string", "\n@attribute additions numeric", "\n@attribute deletions numeric", "\n@attribute changes numeric", "\n@attribute actual_changes string"]
for i in range(127):
	if i == 9:	
		attributes.append("\n@attribute attribute_TAB numeric")
	elif i == 10:
		attributes.append("\n@attribute attribute_NEWLINE numeric")
	elif i == 13:
		attributes.append("\n@attribute attribute_CARRIAGE_RETURN numeric")
	elif (i > 32 and i < 65) or (i > 90 and i < 97) or (i > 122 and i < 127):
		name = unicodedata.name(unicode(chr(i)))
		name = name.replace(" ", "_")
		attributes.append("\n@attribute attribute_%s numeric" % name)

attributes.append("\n@attribute LETTERS_CHANGED numeric")
attributes.append("\n@attribute class {yes, no}")
attributes.append("\n")
attributes.append("\n@data")
for item in attributes:
	text = item
	txt2.write(text) 

filenames = ['monicano.json', 'monicayes.json', 'eno.json', 'eyes.json', 'NEWyes.json', 'NEWno.json']
print "\nThe current list of files to write from is:"
for i in filenames:
	print i
answer = raw_input("\nDo you want to change this list? y/n ")
if answer == 'y':
	filenames = []
	print "Please type 'DONE' when you are done adding files."
	while answer != 'DONE':
		answer = raw_input("\nType the name of the file you want to write from (or type DONE): ")
		if 'yes' not in answer and 'no' not in answer:
			print "\nINVALID FILENAME: The filename needs to have the word 'yes' or 'no' in it."
		elif answer != 'DONE':
			filenames.append(answer)
	print "\nThe current list of files to write from is:"
	for i in filenames:
		print i
print "\nPreparing to write to these files..."


# Edit the keys to make them compatible
answer = raw_input("\nWARNING: \nThe dictionary keys Mistake, Tags, Length, and Why Not will be removed from all of these files to make them compatible with this program. \nKeys will also be modified to add colons if missing. \nPress any key to continue...")
for eachfile in filenames:
	with open(eachfile) as data_file:
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
		if i.get("Tags") != None:
			store = i.get("Tags")
			i.pop("Tags")
			i["Tags:"] = store
			print "Changed one Tags to Tags:"
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
		if i.get("Tags:") != None:
				del i["Tags:"]
	for i in data:
		assert "Additions:" in i
		assert "Deletions:" in i
		assert "Changes:" in i
		assert "Commit Mistakes:" in i
		assert "Commit Corrections:" in i
		assert "Tags:" not in i
		assert "Message:" in i
		assert "Why Not:" not in i
		assert "Mistakes:" not in i
		assert "Length:" not in i
		assert len(i) == 6
	eachfile = open(eachfile, 'w')
	with eachfile as outfile:
		json.dump(data, outfile, indent = 2)
	eachfile.close()
print "\nFiles have been modified.."


# Add the data to the arfffile, but keep track of the links so there are no duplicates.
links = []
yes = 0
no = 0
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
badcharacters = ["'"]
for i in filenames:
	print "\nAdding from %r file.." % i
	txt = open(i, 'a+')
	data = json.load(txt)
	if 'yes' in i:
		chicken = "yes"
	else:
		chicken = "no"
	for thing in data:
		commitlink = thing.get("Commit Corrections:")
		if commitlink in links:
			print "This is a duplicate entry, so I am skipping it."
		else:
			links.append(commitlink)
			changes = thing.get("Changes:")
			additions = []
			deletions = []

			delchar = []
			addchar = []
			chardiff = []
			for i in range(128):
				addchar.append(0)
				delchar.append(0)
				chardiff.append(0)
			for i in changes:
				if str(i[0]) == '+':
					i = i[1:]
					additions.append(i)
				elif str(i[0]) == '-':
					i = i[1:]
					deletions.append(i)
				else:
					print "I didn't recognize %s as a + or a -" % i[0]
			for i in additions:
				for eachletter in i:
					if ord(eachletter) < 128:
						addchar[ord(eachletter)] += 1
			for i in deletions:
				for eachletter in i:
					if ord(eachletter) < 128:
						delchar[ord(eachletter)] += 1
			for i in range(127):
				chardiff[i] = abs(delchar[i] - addchar[i])
			c = 0
			for i in chardiff:
				c += i
			letterschanged = 0
			for i in chardiff:
				if (chardiff.index(i) > 64 and chardiff.index(i) < 91) or (chardiff.index(i) > 96 and chardiff.index(i) < 123):
					letterschanged += 1
			m = thing.get("Message:")
			m = m.encode('ascii', errors='ignore')
			characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
			for letter in m:
				if not(str.lower(letter) in characters):
					m = m.replace(letter, "")
			m = m.replace("'", "")
			m = m.replace("\n", "")
			m = m.replace("class", "")
			a = thing.get("Additions:")
			d = thing.get("Deletions:")
			ch = thing.get("Changes:")
			newletter = None
			newchanges = []
			newitem = None
			for i in ch:
				list1 = []
				for letter in i:
					list1.append(letter)
				if list1[0] == '+' or list1[0] == '-':
					list1.pop(0)
				newchanges.append("".join(list1))
			ch = []
			for i in newchanges:
				ch.append(i)
			newchanges = []
			newletter = None
			characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
			for item in ch:
				for letter in item:
					if letter.lower() not in characters:
						if ord(letter) < 127 and letter != '\n' and letter != '\t' and letter != "\r":
							print "%r" % letter
							newletter = unicodedata.name(unicode(letter))
							newletter = newletter.replace(" ", "_")
							newchanges.append(newletter)
						elif letter == '\n':
							newchanges.append("NEWLINE")
						elif letter == '\t':
							newchanges.append("TAB")
						elif letter == "\r":
							newchanges.append("SLASH_R")
					else:
						newchanges.append(letter)
			string = ""
			good = True
			for i in newchanges:
				if i.lower() not in characters:
					string = " ".join([string, i])
					good = False
				elif good == False:
					string = " ".join([string, i])
					good = True
				else:
					string = "".join([string, i])
					good = True
			string = string.replace("class", "")
			text = "\n"
			stuff = "'%s', %s, %s, %s, '%s'" % (m, a, d, c, string)
			text = "".join([text, stuff])
			counter = 0
			for i in chardiff:
				if counter == 9 or counter == 10 or counter == 13 or (counter > 32 and counter < 65) or (counter > 90 and counter < 97) or (counter > 122 and counter < 127):
					text = ", ".join([text, str(i)])
				counter += 1
			text = ", ".join([text, str(letterschanged)])
			text = ", ".join([text, chicken])
			txt2.write(text)
			txt.close()
			if chicken == 'yes':
				yes += 1
			else:
				no += 1

txt2.close()
	
print "\nAll done! I have added %d yes entries and %d no entries. \nThank you for using %s" % (yes, no, script)

