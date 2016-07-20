# This initiates the thing that connects to the server thing that does a thing
import pymongo
from pymongo import MongoClient

from sys import argv
script, filename = argv
CommitMistakes = ''
CommitCorrections = ''

client = MongoClient('10.13.10.124')
db = client.github
# This is a thing containing all the documents somehow
cursor = db.commits.find()
message = None
parents = None
things = ["indentation", "typo", "bracket", "misspell", "mistake", "syntax", "correct", "corrected", "missed", "minor fixes", "minor changes", "redundant"]
print "============================================"
print "Finding another file just for you..."
print "============================================"

# For each document in cursor...
for document in cursor:
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
		if '.py' in file1:
			if '.py' in file1:
				# For each of the keywords we are looking for...
				for i in things:
					# If it is in the message...
					if i in message:
						print "++++++++++++++++"
						print patch
						print "++++++++++++++++"
						print "\nCommit Message: %s" % message
						print "This is the link to the commit: \n%r" % link
						print "This is the link to the previous commit: \n%r" % parents
						print "This is the file being edited: %r" % file1
						print "Additions: %r" % additions
						print "Deletions: %r" % deletions
						answer = raw_input("Do you want to include this file as an entry? y/n ")
						if answer == 'y':
							txt = open(filename, 'a+')
							CommitMistakes = str(parents)
							CommitCorrections = str(link)
							mistake = raw_input("Type a message for Mistake: ")
							tag = raw_input("Type the Tag: ")
							length = raw_input("Type the length of changes: ")
							if txt.readline(1) != "*":
								txt.write("*" + "\n" "Commit Mistakes:" + "\n" + 									CommitMistakes + "\n" + "Commit Corrections:" + "\n" + 									CommitCorrections + "\n" + "Mistakes:" + "\n" + mistake + 									"\n" + "Tags:" + "\n" + tag + "\n" + "Length:" + "\n" + 								length)
							else:
								txt.write("\n" + "*" + "\n" "Commit Mistakes:" + "\n" + 								CommitMistakes + "\n" + "Commit Corrections:" + "\n" + 									CommitCorrections + "\n" + "Mistakes:" + "\n" + mistake + 									"\n" + "Tags:" + "\n" + tag + "\n" + "Length:" + "\n" + 								length)
							txt.close()
							print "\n============================================"
							print "Finding another file just for you..."
							print "============================================"
						else:
							print "\n============================================"
							print "Finding another file just for you..."
							print "============================================"
						# Don't print it again if it also contains another thing
						break

	

