"""
Merge CSV

Description: Merge CSV files with the same headers into one large CSV file.

Usage: python mergecsv.py data1.csv data2.csv ... dataN.csv
Outs: mergedfile.csv
"""

import sys
import csv

file_iterator = iter(sys.argv)
next(file_iterator) # First one is the name of the script skip it

with open("mergedfile.csv", "wb") as resultFile:
    headers = None
    writer = csv.writer(resultFile)
    for singleFile in file_iterator:
        print "Processing file %s..." % singleFile
        with open(singleFile) as csvFile:
            reader = csv.reader(csvFile)
            local_headers = reader.next()
            if headers is None:
                headers = local_headers
                writer.writerow(headers)
            elif headers != local_headers:
                print "%s does not have same headers" % singleFile
                print "%r does not match %r" % (headers, local_headers)
                raise ValueError("Mismatched headers")
            for row in reader:
                writer.writerow(row)
