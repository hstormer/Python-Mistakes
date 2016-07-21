# This initiates the thing that connects to the server thing that does a thing
import pymongo
from pymongo import MongoClient

# This initiates some variables and gets the file to write things to
from sys import argv
script, filename = argv
CommitMistakes = ''
CommitCorrections = ''

# Accesses database
client = MongoClient()
db = client.github
# This is a thing containing all the documents somehow
cursor = db.commits.find()
#More variable initiation...
counter = 0
save_location = 0
location = 0
name = 'Hannah'
message = None
parents = None
# The list of things we are looking for in the commmit messages
things = ["indentation", "typo", "bracket", "misspell", "mistake", "syntax", "correct", "corrected", "missed", "minor fixes", "minor changes", "redundant", "spelling", "formatter", "stupid"]
# Prints this first so it is separated from the command line and looks nice as it searches
print "============================================"
print "Finding another file just for %s..." % name
print "============================================"

# For each document in cursor...
for document in cursor:
	# If we are at the save location already...
	if save_location == location:
		# Moves location
		save_location += 1
		location += 1
		# This is the commit comment
		message = document.get("commit")
		message = message.get("message")
		# This is the link to the comment
		link = document.get("html_url")
		# These are the changes made in the commit
		patch = document.get("files")
		if patch != [] and patch != None:
			patch = patch[0]
			patch = patch.get("patch")
		# This is the link to the previous commit
		parents = document.get("parents")
		if parents != [] and parents != None:
			parents = parents[0]
			parents = parents.get("html_url")
		# This finds the additions and deletions
		length = document.get("files")
		if length != [] and length != None:
			length = length[0]
			additions = length.get("additions")
			deletions = length.get("deletions")
		# This is the name of the file being edited in the commit
		file1 = document.get("files")
		if file1 != [] and file1 != None:
			file1 = file1[0]
			file1 = file1.get("filename")	
			# If it is a python file with less than 50 deletions and additions...
			if '.py' in file1  and int(additions) < 50 and int(deletions) < 50:
				# For each of the keywords we are looking for...
				for i in things:
					# If it is in the message...
					if i in message:
						# Print changes
						print "++++++++++++++++"
						print patch
						print "++++++++++++++++"
						# Set up the next name
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
						# Print all the commit info
						print "\nCommit Message: %s" % message
						print "This is the link to the commit: \n%r" % link
						print "This is the link to the previous commit: \n%r" % parents
						print "This is the file being edited: %r" % file1
						print "Additions: %r" % additions
						print "Deletions: %r" % deletions
						print "Save location: %d" % (save_location - 1)
						# Check if we have added it to the file already
						txt = open(filename, 'a+')
						if str(link) in txt.read():
								print "WE HAVE ADDED THIS ALREADY!"
						txt.close()
						# Should we include this?
						answer = raw_input("Do you want to include this file as an entry? y/n ")
						if answer == 'y':
							# Write the file! :D
							txt = open(filename, 'a+')
							CommitMistakes = str(parents)
							CommitCorrections = str(link)
							mistake = raw_input("Type a message for Mistake: ")
							tag = raw_input("Type the Tag: ")
							length = raw_input("Type the length of changes: ")
							# If this is the first entry, do not do a newline
							if txt.readline(1) != "*":
								txt.write("*" + "\n" "Commit Mistakes:" + "\n" + 								CommitMistakes + "\n" + "Commit Corrections:" + "\n" + 								CommitCorrections + "\n" + "Mistakes:" + "\n" + mistake + 								"\n" + "Tags:" + "\n" + tag + "\n" + "Length:" + "\n" + 							length)
							else:
								txt.write("\n" + "*" + "\n" "Commit Mistakes:" + "\n" + 							CommitMistakes + "\n" + "Commit Corrections:" + "\n" + 								CommitCorrections + "\n" + "Mistakes:" + "\n" + mistake + 								"\n" + "Tags:" + "\n" + tag + "\n" + "Length:" + "\n" + 							length)
							txt.close()
							# Close the file and find another commit
							print "\n============================================"
							print "Finding another file just for %s..." % name
							print "============================================"
						else:
							print "\n============================================"
							print "Finding another file just for %s..." % name
							print "============================================"
						# Don't print it again if it also contains another thing
						break
	# Change the location by one if we were not at the save location
	else: 
		location += 1

	

