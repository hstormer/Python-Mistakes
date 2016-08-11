# This initiates the thing that connects to the server thing that does a thing
import pymongo
import json
from pymongo import MongoClient

from sys import argv
script, filename, secondfile = argv
CommitMistakes = ''
CommitCorrections = ''

def housecleaning(l):
	finalist = []
	list1 = []
	finish = []
	templist = []
	for line in l:
		list1.append(line)
	for i in list1:
		templist.append(i)
		if i.encode('utf8') == '\n':
			str1 = ''.join(templist)
			templist = []
			finalist.append(str1)
	str1 = ''.join(templist)
	finalist.append(str1)
	finalist.pop(0)
	list1 = []
	for i in finalist:
		list1 = []
		for line in i:
			list1.append(line)
		templist = []
		if str(list1[0])== '+' or str(list1[0]) == '-':
			str1 = ''.join(list1)
			finish.append(str1)
	return finish

client = MongoClient()
db = client.github
# This is a thing containing all the documents somehow
cursor = db.commits.find()
jsonfile = {}
entries = []
counter = 0

print "I will write the 'yes' entries to the %s file. \nI will write the 'no' entries to the %s file." % (filename, secondfile)

save_location = raw_input("Do you have a save location? y/n  ")
if save_location == 'y':
	save_location = int(raw_input("Please enter your save location:  "))
	print "Starting from save location %d..." % save_location
else:
	save_location = 0
	print "Starting from the beginning of the dataset..."

location = 0
name = 'Hannah'
message = None
parents = None
things = ["indentation", "typo", "bracket", "misspell", "mistake", "syntax", "correct", "corrected", "missed", "minor fixes", "minor changes", "redundant", "spelling", "formatter", "stupid"]
print "============================================"
print "Finding another file just for %s..." % name
print "============================================"

# For each document in cursor...
for document in cursor:
	if save_location == location:
		save_location += 1
		location += 1
		# This is the commit comment
		message = document.get("commit")
		message = message.get("message")
		# This is the link to the comment
		link = document.get("html_url")
		patch = document.get("files")
		if patch != [] and patch != None:
			patch = patch[0]
			patch = patch.get("patch")
		parents = document.get("parents")
		if parents != [] and parents != None:
			parents = parents[0]
			parents = parents.get("html_url")
		length = document.get("files")
		if length != [] and length != None:
			length = length[0]
			additions = length.get("additions")
			deletions = length.get("deletions")
		file1 = document.get("files")
		if file1 != [] and file1 != None:
			file1 = file1[0]
			file1 = file1.get("filename")	
			if '.py' in file1  and int(additions) < 50 and int(deletions) < 50:
				# For each of the keywords we are looking for...
				for i in things:
					# If it is in the message...
					if i in message or (int(additions) == 1 and int(deletions) ==1):
						print "++++++++++++++++"
						print patch
						print "++++++++++++++++"
						counter += 1
						if counter == 4:
							counter = 1
						if counter == 1:
							print "This is Hannah's."
							name = 'Monica'
						if counter == 2:
							print "This is Monica's."
							name = 'Eisha'
						if counter == 3:
							print "This is Eisha's."
							name = 'Hannah'
						if int(additions) == 1 and int(deletions) ==1:
							print "\nKeyword found: Length"
							i = "length"
						else:
							print "\nkeyword found: " + i
						print "\nCommit Message: %s" % message
						print "This is the link to the commit: \n%r" % link
						print "This is the link to the previous commit: \n%r" % parents
						print "This is the file being edited: %r" % file1
						print "Additions: %r" % additions
						print "Deletions: %r" % deletions
						print "Save location: %d" % (save_location - 1)
						txt = open(filename, 'a+')
						if str(link) in txt.read():
								print "WE HAVE ADDED THIS ALREADY!"
								break
						txt.close()
						txt2 = open(secondfile, 'a+')
						if str(link) in txt2.read():
								print "WE HAVE ADDED THIS ALREADY!"
								break
						txt2.close()
						answer = raw_input("Do you want to include this file as an entry? y/n ")
						if answer == 'y':
							txt = open(filename, 'a+')
							CommitMistakes = str(parents)
							CommitCorrections = str(link)
							patch = housecleaning(patch)
							data = {"Commit Mistakes:" : CommitMistakes, "Commit Corrections:" : CommitCorrections, "Additions": additions, "Deletions:": deletions, "Changes:" : patch, "Message:" : message}
							entries.append(data)
							with open(filename) as f:
								try:
									entries = json.load(f)
								except ValueError:
									entries = []
								
							txt.seek(0)
							txt.truncate()
							entries.append(data)
							with open(filename, 'a+') as outfile:
								json.dump(entries, outfile, indent = 2)
							print "\n============================================"
							print "Finding another file just for %s..." % name
							print "============================================"
						elif answer == 'n':
							txt2 = open(secondfile, 'a+')
							CommitMistakes = str(parents)
							CommitCorrections = str(link)
							patch = housecleaning(patch)
							print patch
							data = {"Commit Mistakes:" : CommitMistakes, "Commit Corrections:" : CommitCorrections, "Additions:": additions, "Deletions:": deletions, "Changes:" : patch, "Message:" : message}
							entries.append(data)
							with open(secondfile) as f:
								try:
									entries = json.load(f)
								except ValueError:
									entries = []
							txt2.seek(0)
							txt2.truncate()
							entries.append(data)
							with open(secondfile, 'a+') as outfile:
								json.dump(entries, outfile, indent = 2)
							print "\n============================================"
							print "Finding another file just for %s..." % name
							print "============================================"
						else:
							None
						# Don't print it again if it also contains another thing
						break
	else: 
		location += 1

	

