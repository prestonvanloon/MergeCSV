"""
Merge CSV

Description: Merge CSV files with the same headers into one large CSV file.

Usage: python mergecsv.py data1.csv data2.csv ... dataN.csv
Outs: mergedfile.csv
"""

import sys
import csv

class MergeUnit(object):
    """  """
    values = []
    langs = []

    def __init__(self, values, numOfLanguages):
        self.values = values
        self.langs = [""] * numOfLanguages

    def is_equal(self, values):
        """ Equaliy comparator """
        return self.values == values

    def set_language_value_at_index(self, value, index):
        """ Sets value at index """
        self.langs[index] = value

    def to_csv(self):
        """ Returns a csv row string """
        return ",".join(self.values + self.langs)

file_iterator = iter(sys.argv)
next(file_iterator) # First one is the name of the script skip it

headers_to_match = []
languages = []

def add_unique_to_array(array, value):
    """ Adds value to array if does not exist """
    try:
        array.index(value)
    except:
        array.append(value)

for singleFile in file_iterator:
    if singleFile.endswith('.csv'):
        print "Processing file " + singleFile + "..."
        with open(singleFile) as csvfile:
            isLanguageName = False
            for header in csvfile.readline().split(','):
                headerStripped = header.strip()
                if not isLanguageName:
                    if headerStripped == "KEY":
                        isLanguageName = True
                    add_unique_to_array(headers_to_match, headerStripped)
                else:
                    add_unique_to_array(languages, headerStripped)

final_headers = headers_to_match + languages
merged_cells = []

lang_index = 0
for singleFile in iter(sys.argv):
    if singleFile.endswith('.csv'):
        headers = []
        with open(singleFile) as csvfile:
            headers = csvfile.readline().strip('\n').split(',')
            reader = csv.DictReader(csvfile, headers, delimiter=",")

            for row in reader:
                langValue = None
                values = []
                for header in headers_to_match:
                    values.append(row[header])
                for lang in languages:
                    if row.has_key(lang):
                        langValue = row[lang]
                hasMergedForValue = False
                for merged in merged_cells:
                    if merged.is_equal(values):
                        hasMergedForValue = True
                        merged.set_language_value_at_index(langValue, lang_index)
                if not hasMergedForValue:
                    merged = MergeUnit(values, len(languages))
                    merged.set_language_value_at_index(langValue, lang_index)
                    merged_cells.append(merged)
            lang_index = lang_index + 1

with open("mergedfile.csv", "wb") as resultFile:
    resultFile.write(",".join(final_headers)+ "\n")
    for merged in merged_cells:
        resultFile.write(merged.to_csv() + "\n")
