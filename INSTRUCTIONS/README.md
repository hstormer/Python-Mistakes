Python-Mistakes INSTRUCTIONS
==========================================================================================================================

TO COLLECT NEW ENTRIES:
1. Make sure that you have two json files, one to store 'yes' entries and one to store 'no' entries. You can collect entries onto an existing file of entries, or create a new empty file. If you plan to add the data from these files directly to the arff file, make sure the yes file has 'yes' in the filename and the no file has 'no' in the name.

![Alt text](/INSTRUCTIONS/fig1.png?raw=true "FIGURE 1")

2. Run "python DATACOLLECT.py <yesfile> <nofile>" to collect data for yes and no entries. Make sure you have pymongo installed and that there is a database of github commits from MongoDB downloaded. 

![Alt text](/INSTRUCTIONS/fig2.png?raw=true "FIGURE 2")

3. The program will keep track of a save location number so you can start collecting data from the same place you left off. The number will be displayed each time it finds a commit. The program will prompt you for this number when you run it. Please write the save location number down somewhere so you can enter it in the program if you wish to start collecting data from the same location the next time you run the program.

![Alt text](/INSTRUCTIONS/fig3.png?raw=true "FIGURE 3")

TO RECORD ENTRIES IN THE ARFF FILE:

1. Run "python WRITER6.py <name of arff file>" to upload the data into the arff file. The program starts with a list of files to upload from, but will prompt you to change this list if you wish.

![Alt text](/INSTRUCTIONS/fig4.png?raw=true "FIGURE 4")

You can also go into the program and replace the list if you are going to be adding from the same files many times. 

![Alt text](/INSTRUCTIONS/fig5.png?raw=true "FIGURE 5")

There are also other WRITER programs that add different combination of attributes. WRITER6 is the most recent version of the program. Each writer program has a description at the top of what attributes it will add.

![Alt text](/INSTRUCTIONS/fig6.png?raw=true "FIGURE 6")

2. Please note that WRITER6 will modify all files that are added to the arff file by deleting duplicate entries and modifying the keys. It will also remove any extra values.

RUNNING WEKA:

1. Run the wekadatatest.arff file (or where ever you stored your entries. For Classifiers, use FilteredClassifier and make sure the filter under it is set to StringToWordVector. 

2. Under StringToWordVector, make sure the stop list is True (I've been using Rainbow)

3. The classifier you'll use under FilteredClassifier is Vote. Under Vote, set the combinationRule to Majority Voting.



Enjoy :)
