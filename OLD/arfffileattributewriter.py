#this file will write the commit messages, additions, deletions, and length to the mistakes.arff file. Also a looooot of attributes (this is the first version using ascii)


attributes = ["\n@relation python_mistakes", "\n", "\n@attribute commit_message string", "\n@attribute additions numeric", "\n@attribute deletions numeric", "\n@attribute changes numeric"]

from sys import argv
script, filename, arff_file = argv

answer = raw_input("WARNING! THIS WILL OVERWRITE THE ARFF FILE!")

txt2 = open(arff_file, 'w')
text = ''

for i in range(128):
	attributes.append("\n@attribute attribute_%d numeric" % i)

attributes.append("\n@attribute class {yes, no}")
attributes.append("\n")
attributes.append("\n@data")
	
for item in attributes:
	text = item
	txt2.write(text) 


import json
import codecs

filenames = ['monicano.json', 'monicayes.json', 'eno.json', 'eyes.json', 'NEWyes.json', 'NEWno.json']
arfffile = 'wekadatatest.arff'

x = raw_input("Make sure you have DELETED the contents of the %s file, otherwise it will just add these onto the end, and we will have duplicate entries. Press any key to continue..." %arfffile)

for i in filenames:
	print i
	txt = open(i, 'a+')
	print txt
	data = json.load(txt)
	characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']

	badcharacters = ["'"]

	if 'yes' in i:
		chicken = "yes"
	else:
		chicken = "no"

	for thing in data:
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
		print chardiff
		c = 0
		for i in chardiff:
			c += i
		m = thing.get("Message:")
		m = m.encode('ascii', errors='ignore')
		for letter in m:
			if not(str.lower(letter) in characters):
				m = m.replace(letter, "")
				print letter
		m = m.replace("'", "")
		m = m.replace("\n", "")
		m = m.replace("class", "")
		a = thing.get("Additions:")
		d = thing.get("Deletions:")
		text = "\n"
		stuff = "'%s', %s, %s, %s" % (m, a, d, c)
		text = "".join([text, stuff])
		for i in chardiff:
			text = ", ".join([text, str(i)])
		text = ", ".join([text, chicken])
		txt2.write(text)

txt2.close()
	
			

