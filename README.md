MergeCSV
========

Python script to merge localization CSV files.

Requirements:

1) Each CSV file must contain only the BUILD_TRAIN, MILESTONE, KEY and the respective language column
2) The exact same number of rows.

There are two versions of the script, one to specify each file individually and the other for batch processing all CSV files in a directory.

Tip: It’s easier to just copy and run the script in the same directory containing the CSV files you want to merge, instead of specifying the path in the command line.

Syntax:

Individual files (you can combine any number of files):
=======

python cvsmerge_simple.py Greek_Sample.csv Slovak_Sample.csv

Batch processing:
=======
Syntax for batch processing (all CSV files in the directory will be merged):

python csvmerge_wilcard.py './*.csv'

Note that the expression needs to be in quotes (do not copy and paste the quotes, type them in Terminal)

------------------------------------------------

This is what the merged file looks like:

BUILD_TRAIN,MILESTONE,KEY,GREEK,SLOVAK
nonononono,14D,key.three,Προεπιλογές,Predvoľby
nonononono,14D,key.one,"Τη στιγμή του γεγονότος","V čase"
nonononono,14D,key.two,"Προσθήκη γεγονότων και προσκλήσεων σε:","Udalosti a pozvánky pridávať do:"
------------------------------------------------

If you want to change the delimiter type on the merged file, modify delimiter=',' on line 37:
