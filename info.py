from sys import argv

# Run the program with the name of the file to open after the script name (in this case test.txt)
script, open_file = argv

# txt is the file
txt = open(open_file)
# These are the two variables that are added to the dictionary. text is the line after key.
key = None
text = 1
# This is the list that stores the dictionary for each entry in test.txt
listofdictionaries = []
# This is the dictionary used to store the info from each entry. It is replaced each time the loop runs for each entry after it is added to the listofdictionaries.
dictionary1 = {}

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

# While the end of the file isn't reached...
while str(text) != '#':
	# While the end of the entry isn't reached...
	while str(key) != '*\n':
		key = txt.readline()
		key = housecleaning(key)
		text = txt.readline()
		text = housecleaning(text)
		if str(text) != '*\n' and str(text) != '*' and str(key) != '*\n' and str(key) != '*':
			dictionary1[key] = text
		else:
			break
	# The end of the entry is reached, but is it the end of the file?
	if str(text) != '#':
		listofdictionaries.append(dictionary1)
		dictionary1 = {}
		key = text
		key = housecleaning(text)
		text = txt.readline()
		text = housecleaning(text)
		if str(text) != '*\n' and str(text) != '*' and str(key) != '*\n' and str(key) != '*':
			dictionary1[key] = text
	# Yes, it is the end of the file. Add the dictionary to listofdictionaries and stop the loop.
	else:
		listofdictionaries.append(dictionary1)


#print "==============="
#print "This is the complete list of dictionaries: %r" % listofdictionaries
#print "==============="
dictionary1 = listofdictionaries[0]
print "This is the dictionary for the first entry: %r" % dictionary1
print "==============="
#When searching for something, put the name and :.
print "This is the first entry's Commit Corrections link: %s" % dictionary1["Commit Corrections:"]

	
