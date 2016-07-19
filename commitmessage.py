# This initiates the thing that connects to the server thing that does a thing
import pymongo
from pymongo import MongoClient
client = MongoClient('10.13.10.124')
db = client.github
# This is a thing containing all the documents somehow
cursor = db.commits.find()
message = None
things = ["indentation", "typo", "bracket", "misspell", "mistake", "syntax", "correct", "corrected", "missed", "minor fixes", "minor changes", "redundant"]

# For each document in cursor...
for document in cursor:
	# This is the commit comment
	message = document.get("commit")
	message = message.get("message")
	# This is the link to the comment
	#link = document.get("html_url")
	#print link
	# For each of the keywords we are looking for...
	for i in things:
		# If it is in the message...
		if i in message:
			print message
	#		print link
			print "============================================"
			# Don't print it again if it also contains another thing.
			break
