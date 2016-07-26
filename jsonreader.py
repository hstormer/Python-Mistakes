from sys import argv
import json

item = None

# Run the program with the name of the file to open after the script name (in this case test.txt)
file1 = raw_input("Which file do you want to read?: ")


with open(file1) as data_file:
	data = json.load(data_file)

print data[0]
item = data[0]
print len(data)
print item
print item.get("Commit Mistakes")

	
