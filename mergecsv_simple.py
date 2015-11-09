import sys
import csv
import glob

class MergeUnit():
    values = []
    langs = []
    
    def __init__(self, values, numOfLanguages):
        self.values = values
        self.langs = [""] * numOfLanguages
    
    def isEqual(self, values):
        return self.values == values

    def setLanguageValueAtIndex(self, value, index):
        self.langs[index] = value 

    def toCSV(self):
        return ",".join(self.values + self.langs)

fileInterator = iter(sys.argv)
next(fileInterator) # First one is the name of the script skip it

lookupMap = {}

headersToMatch = []
languages = []

def addUniqueToArray(array, value):
    try:
        array.index(value)
    except:
        array.append(value)
        pass
    

for singleFile in fileInterator:
    if singleFile.endswith('.csv'):
        print "Processing file " + singleFile + "..."
        with open(singleFile) as csvfile:
            isLanguageName = False
            for header in csvfile.readline().split(','):
                headerStripped = header.strip()
                if not isLanguageName:
                    if headerStripped == "KEY":
                        isLanguageName = True
                    addUniqueToArray(headersToMatch, headerStripped)
                else:
                    addUniqueToArray(languages, headerStripped)    

finalHeaders = headersToMatch + languages
mergedCells = []

langIndex = 0
for singleFile in iter(sys.argv):
    if singleFile.endswith('.csv'):
        headers = []
        with open(singleFile) as csvfile:
            headers = csvfile.readline().strip('\n').split(',')
            reader = csv.DictReader(csvfile, headers, delimiter=",")
            
            for row in reader:
                langValue = None
                values = []
                for header in headersToMatch:
                    values.append(row[header])
                for lang in languages:
                    if row.has_key(lang):
                        langValue = row[lang]
                hasMergedForValue = False
                for merged in mergedCells:
                    if merged.isEqual(values):
                        hasMergedForValue = True
                        merged.setLanguageValueAtIndex(langValue, langIndex)    
                if not hasMergedForValue:
                    merged = MergeUnit(values, len(languages))
                    merged.setLanguageValueAtIndex(langValue, langIndex)
                    mergedCells.append(merged)
            langIndex = langIndex + 1 
                        

with open("mergedfile.csv", "wb") as resultFile:
    resultFile.write(",".join(finalHeaders)+ "\n")
    for merged in mergedCells:
        resultFile.write(merged.toCSV() + "\n")
#             
# 
# 
# finalHeader =["KEY"]
# for singleFile in fileInterator:
#     print "Processing file " + singleFile + "...."
#     with open(singleFile) as csvfile:
#         # Get the language name and append to header to be used later
#         finalHeader.append(csvfile.readline().split(",")[1].rstrip('\r\n'))
# 
#     with open(singleFile) as csvfile:
#         reader = csv.DictReader(csvfile,'KEY LANGUAGE'.split(), delimiter=',')
#         next(csvfile) # Skip reading the first line this the header
#         for row in reader:
#             if row["KEY"] in lookupMap:
#                 lookupMap[row["KEY"]].append(row["LANGUAGE"])
#             else:
#                 lookupMap[row["KEY"]] = [row["LANGUAGE"]]
# print "Done processing all files, attempting to create merged file" + "\n"
# 
# finalResult =[]
# finalResult.append(finalHeader)
# for key in lookupMap:
#     row = []
#     row.append(key)
#     row.extend(lookupMap[key])
#     finalResult.append(row)
# 
# # print finalResult
# # print finalHeader
# with open("mergedfile.csv", "wb") as resultfile:
#     w = csv.writer(resultfile, delimiter=',')
#     w.writerows(finalResult)
# 
# print "Merged file created. Look for mergedfile.csv on current path"

