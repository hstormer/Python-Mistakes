# This initiates the thing that connects to the server thing that does a thing
import pymongo
from pymongo import MongoClient
client = MongoClient('10.13.10.124')
db = client.github
# This is a thing containing all the documents somehow
cursor = db.commits.find()
message = None
things = ["indentation", "typo", "bracket", "misspell", "mistake", "syntax", "correct", "corrected", "missed", "minor fixes", "minor changes", "redundant"]
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
	file1 = document.get("files")
	if file1 != [] and file1 != None:
		file1 = file1[0]
		file1 = file1.get("filename")	
		if '.py' in file1:
			# For each of the keywords we are looking for...
			for i in things:
				# If it is in the message...
				if i in message:
					print "Commit Message: %r" % message
					print "\n++++++++++++++++"
					print patch
					print "++++++++++++++++\n"
					print "This is the link to the commit: \n%r" % link
					print "This is the file being edited: %r" % file1
					print "\n============================================"
					answer = raw_input("Press something to continue printing...")
					print "============================================\n"
					# Don't print it again if it also contains another thing.
					break

