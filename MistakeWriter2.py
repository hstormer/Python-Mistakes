#this file will write the commit messages, additions, deletions, and length to the mistakes.arff file


import json

from sys import argv
script, filename, arff_file = argv

txt = open(filename, 'a+')
txt2= open(arff_file, 'a+')
data = json.load(txt)

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']

badcharacters = ["'"]

print "Are you using the yes.json or no.json?" 
ans = raw_input("y/n ")
if str(ans) == "y":
	chicken = "yes"
else:
	chicken = "no"

for i in data:
	#c = str(i.get("Changes:"))
	m = i.get("Message:")
	m = m.encode('ascii', errors='ignore')
	for letter in m:
		if not(str.lower(letter) in characters):
			m = m.replace(letter, "")
			print letter
	m = m.replace("'", "")
	m = m.replace("\n", "")
	m = m.replace("class", "")
	a = i.get("Additions:")
	d = i.get("Deletions:")
	text = "\n'%s', %s, %s, %s" %(m,a,d,chicken)
	text = text.encode('ascii', errors='ignore')
	text = str(text)
	txt2.write(text)

txt2.close()
	
			

