from sys import argv
import json

answer = raw_input("WARNING! THIS WILL DELETE THE CONTENTS OF THE JSONTEST.JSON FILE! IF YOU DO NOT WANT THIS TO HAPPEN, PLEASE PRESS ^C TO STOP THE PROGRAM!")	

# Run the program with the name of the file to open after the script name (in this case test.txt)
filename = raw_input("Which file to write to and remove colons from?: ")

# txt is the file
open_file = open(filename, 'a+')
print open_file
# These are the two variables that are added to the dictionary. text is the line after key.
key = None
text = 1
# This is the list that stores the dictionary for each entry in test.txt
listofdictionaries = []
# This is the dictionary used to store the info from each entry. It is replaced each time the loop runs for each entry after it is added to the listofdictionaries.
dictionary1 = {}
counter = 2


# This removes the \n from each line.
def housecleaning(l):
	list1 = list(l)
	# This makes sure it doesn't try to pop a blank list. 
	if list1 != []:
		list1.pop()
		str1 = ''.join(list1)
	# This makes sure the loop ends when it reaches a blank line or the *
	else:
		str1 = '*\n'
	return str1

def colongone(l):
	list1 = list(l)
	str1 = l
	if list1 != []:
		if str(list1[-1]) == ':':
			list1.pop()
			str1 = ''.join(list1)
	# This makes sure the loop ends when it reaches a blank line or the *
	else:
		str1 = '*\n'
	return str1
while str(text) != '#':
	while str(key) != '*\n':
		key = open_file.readline()
		key = housecleaning(key)			
		text = open_file.readline()
		text = housecleaning(text)
		key = colongone(key)
		text = colongone(text)
		if str(text) != '*\n' and str(text) != '*' and str(key) != '*\n' and str(key) != '*':
			dictionary1[key] = text
		else:
			break
	if str(text) != '#':
		listofdictionaries.append(dictionary1)
		dictionary1 = {}
		key = text
		key = housecleaning(text)
		text = open_file.readline()
		text = housecleaning(text)
		if str(text) != '*\n' and str(text) != '*' and str(key) != '*\n' and str(key) != '*':
			dictionary1[key] = text
	else:
		listofdictionaries.append(dictionary1)


#print "==============="
#print "This is the complete list of dictionaries: %r" % listofdictionaries
#print "==============="
dictionary1 = listofdictionaries[0]
print "This is the dictionary for the first entry: %r" % dictionary1
print "==============="
#When searching for something, put the name and :.
print "This is the first entry's Commit Corrections link: %s" % dictionary1["Commit Corrections"]
print "This is the number of entries: %r" % len(listofdictionaries)

with open_file as outfile:
	json.dump(listofdictionaries, outfile, indent = 2)


	
