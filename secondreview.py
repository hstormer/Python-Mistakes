# This initiates the thing that connects to the server thing that does a thing
import pymongo
from pymongo import MongoClient

from sys import argv
script, filename , secondfile = argv
CommitMistakes = ''
CommitCorrections = ''

client = MongoClient()
db = client.github
# This is a thing containing all the documents somehow
cursor = db.commits.find()
counter = 0
save_location = 0
location = 0
name = 'Hannah'
things = ["indentation", "typo", "bracket", "misspell", "mistake", "syntax", "correct", "corrected", "missed", "minor fixes", "minor changes", "redundant", "spelling", "formatter", "stupid", "version", "bump", "merge", "merging", "comment", "test", "testing", "renamed"]
message = None
parents = None
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
			if '.py' in file1  and int(additions) == 1 and int(deletions) == 1:
				show = True				
				for i in things:
					if i in message.lower():
						show = False
						break
				if show == True:
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
						mistake = raw_input("Type a message for Mistake: ")
						tag = raw_input("Type the Tag: ")
						length = raw_input("Type the length of changes: ")
						data = {"Commit Mistakes" : CommitMistakes, "Commit Corrections:" : CommitCorrections, "Mistake:" : mistake, "Tags:" : tag, "Length": length, "Keyword:" : i}
						entries.append(data)
						with open('jsontest.json') as f:
							entries = json.load(f)
						print entries
						txt.seek(0)
						txt.truncate()
						entries.append(data)
						with open('jsontest.json', 'a+') as outfile:
							json.dump(entries, outfile, indent = 2)
						print "\n============================================"
						print "Finding another file just for %s..." % name
						print "============================================"
					else:
						txt2 = open(secondfile, 'a+')
						CommitMistakes = str(parents)
						CommitCorrections = str(link)
						why_not = raw_input("Why did you not include this file? ")
						data = {"Commit Mistakes" : CommitMistakes, "Commit Corrections:" : CommitCorrections, "Why Not:" : why_not, "Keyword:" : i, "Additions": additions, "Deletions:": deletions}
						entries.append(data)
						with open('jsonno.json') as f:
							entries = json.load(f)
						print entries
						txt2.seek(0)
						txt2.truncate()
						entries.append(data)
						with open('jsonno.json', 'a+') as outfile:
							json.dump(entries, outfile, indent = 2)
						print "\n============================================"
						print "Finding another file just for %s..." % name
						print "============================================"
	else: 
		location += 1

print location
print save_location

