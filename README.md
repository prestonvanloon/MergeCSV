MergeCSV
========

Python script to merge CSV files.

Requirements:

1) Each CSV file must contain the same ordered column headers
2) The first row must be the column header on each CSV file.


Syntax:

```
python mergecsv.py fileA.csv fileB.csv fileC.csv

```

The result is `mergedfile.csv` with all of the rows concatenated into one CSV file.