from sys import argv
import json

item = None

# Run the program with the name of the file to open after the script name (in this case test.txt)
script, open_file = argv

with open('jsontest.json') as data_file:
	data = json.load(data_file)

print data[0]
item = data[0]
print item
print item.get("Commit Mistakes")

	
