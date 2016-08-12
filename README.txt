Python-Mistakes INSTRUCTIONS
==========================================================================================================================

TO COLLECT NEW ENTRIES:
1. Make sure that you have two json files, one to store 'yes' entries and one to store 'no' entries. 
![Alt text](/INSTRUCTIONS/fig1.jpg?raw=true "Fig1")
You can collect entries onto an existing file of entries, or create a new empty file. If you plan to add the data from these files directly to the arff file, make sure the yes file has 'yes' in the filename and the no file has 'no' in the name.

2. Run "python DATACOLLECT.py <yesfile> <nofile>" to collect data for yes and no entries. Make sure you have pymongo installed and that there is a database of github commits from MongoDB downloaded. 

3. The program will keep track of a save location number so you can start collecting data from the same place you left off. The number will be displayed each time it finds a commit. The program will prompt you for this number when you run it. Please write the save location number down somewhere so you can enter it in the program if you wish to start collecting data from the same location the next time you run the program.

TO RECORD ENTRIES IN THE ARFF FILE:

1. Run "python WRITER6.py <name of arff file>" to upload the data into the arff file. The program starts with a list of files to upload from, but will prompt you to change this list if you wish (or you can go into the program and replace the list if you are going to be adding from the same files many times). There are also other WRITER programs that add different combination of attributes. WRITER6 is the most recent version of the program. Each writer program has a description at the top of what attributes it will add.

2. Please note that WRITER6 will modify all files that are added to the arff file by deleting duplicate entries and modifying the keys. It will also remove any extra values.

Enjoy :)
