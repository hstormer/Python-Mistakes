#this file will write the commit messages, additions, deletions, and length to the mistakes.arff file


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

for i in data:
	if i.get("Message:") != None:
		m = str(i.get("Message:"))
	else:
		m = "?"
	if i.get("Additions:") != None:
		a = str(i.get("Additions:"))
	else:
		a = "?"
	if i.get("Deletions:") != None:
		d = str(i.get("Deletions:"))
	else:
		d = "?"
	if i.get("Length") != None:
		l = str(i.get("Length"))
	else:
		l = "?"

	#if m in data and a in data and d in data:

	if m == "?":
		txt2.write("\n?, %s, %s, %s, %s" %(a,d,l,chicken) )
		print '?, %s, %s, %s, %s' %(a,d,l,chicken) 
	else:	
		txt2.write("\n%r, %s, %s, %s, %s" %(m,a,d,l,chicken) )
		print '%s, %s, %s, %s, %s' %(m,a,d,l,chicken) 

txt2.close()
	
			

