#this file will write the specific changes to the arff file


import json

from sys import argv
script, filename, arff_file = argv

txt = open(filename, 'a+')
txt2= open(arff_file, 'a+')
data = json.load(txt)

print "Are you using the yes.json or no.json?" 
ans = raw_input("y/n ")
if str(ans) == "y":
	chicken = "yes"
else:
	chicken = "no"

counter = 0
LENGTHOFCHANGES = 0

print "=========================================================="

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '.']

for thing in data:
	changes = thing.get("Changes:")
	counter = 0
	LENGTHOFCHANGES = 0

	while len(changes) != 0 and len(changes) != 1:
		diff1 = []
		diff2 = []
		close = []
		least = 2000
		for i in changes:
			close.append(len(i))
		print close
		for i in close:
			# Holds the item it is looking at, so it doesn't compare to itself
			hold = i
			close.remove(i)
			for otheritems in close:
				if (abs(i-otheritems)) < least:
					least = (abs(i-otheritems))
					diff1 = []
					diff2 = []
					diff1.append(i)
					diff2.append(otheritems)
					close.remove(otheritems)
					hold = 300000
			# Don't add myself back in, already been looked at.
			if hold != 300000:
				close.append(hold)

		for i in changes:
			if len(i) == diff1[0]:
				diff1 = []
				for letter in i:
					diff1.append(letter)
				changes.remove(i)
		for i in changes:
			if len(i) == diff2[0]:
				diff2 = []
				for letter in i:
					diff2.append(letter)
				changes.remove(i)
		print "The first line to compare: %r" % "".join(diff1)
		print "The second line to compare: %r" % "".join(diff2)

		if diff1[0] == '+' or diff1[0] == '-':
			diff1.pop(0)
		if diff2[0] == '+' or diff2[0] == '-':
			diff2.pop(0)
		run = True
		while run:
			if len(diff2) != 0 and len(diff1) != 0:
				if diff1[0] == diff2[0]:
					diff1.pop(0)
					diff2.pop(0)
				else:
					run = False
			else:
				run = False
		run = True
		while run:
			if len(diff2) != 0 and len(diff1) != 0:
				if diff1[-1] == diff2[-1]:
					diff1.pop(-1)
					diff2.pop(-1)
				else:
					run = False
			else: 
				run = False
		print "The differences:"
		print "%s" % "".join(diff1)
		m = "%s" % "".join(diff1)
		print "%s" % "".join(diff2)
		j = "%s" % "".join(diff2)
		counter += 1
		LENGTHOFCHANGES += len(diff1)
		LENGTHOFCHANGES += len(diff2)
		print "Length of changes so far: %r" % LENGTHOFCHANGES
		print "========================"

		m = m.encode('ascii', errors='ignore')
		j = j.encode('ascii', errors='ignore')
		for letter in m: 
			if not (str.lower(letter) in characters):
				b = m.replace(letter, "")
				print "CHANGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEED"
				print letter
				print b
			else:
				print letter
	

		for letter in j: 
			if not (str.lower(letter) in characters):
				k = m.replace(letter, "")
				print "CHANGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEED"
				print letter
				print k
			else:
				print letter

		
		#text =  "\n%s, %s, %s" %(b,k,chicken)
		#text = text.encode('ascii', errors='ignore')
		#text = str(text)
		#txt2.write(text)
	print "#############################################################################################################################"
	print b
	print k 
	print "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"

	if len(changes) == 1:
		print "The differences:"
		print "%r" % changes[0]
		LENGTHOFCHANGES += len(changes[0])

	print "Total differences: %d" % LENGTHOFCHANGES


