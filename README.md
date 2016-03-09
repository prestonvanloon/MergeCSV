MergeCSV
========

Python script to merge localization CSV files.

Requirements:

1) Each CSV file must contain only the BUILD_TRAIN, MILESTONE, KEY and the respective language column. If needed, remove the following columns from all files: ENGLISH, EXPLANATION, COMMENT and TRANSLATION_STATUS.<br>
2) The exact same number of rows.


Syntax:

Tip: It’s easier to just copy and run the script in the same directory containing the CSV files you want to merge, instead of specifying the path in the command line.

Individual files (you can combine any number of files):
=======

```
python mergecsv.py Greek_Sample.csv Slovak_Sample.csv

```

Note: The expression needs to be in quotes (do not copy and paste the quotes, type them in Terminal)

------------------------------------------------

This is what the merged file looks like:
```
BUILD_TRAIN,MILESTONE,KEY,GREEK,SLOVAK
nonononono,14D,key.three,Προεπιλογές,Predvoľby
nonononono,14D,key.one,"Τη στιγμή του γεγονότος","V čase"
nonononono,14D,key.two,"Προσθήκη γεγονότων και προσκλήσεων σε:","Udalosti a pozvánky pridávať do:"

```
------------------------------------------------

If you want to change the delimiter type on the merged file, modify delimiter=',' on line 37:
