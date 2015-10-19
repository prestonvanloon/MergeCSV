import sys
import csv
import glob

fileInterator = glob.glob(sys.argv[1]) # Reading the expression for file search

lookupMap = {}

finalHeader =["KEY"]
for singleFile in fileInterator:
	print "Processing file " + singleFile + "...."
	with open(singleFile) as csvfile:
		# Get the language name and append to header to be used later
		finalHeader.append(csvfile.readline().split(",")[1].rstrip('\r\n'))

	with open(singleFile) as csvfile:
		reader = csv.DictReader(csvfile,'KEY LANGUAGE'.split(), delimiter=',')
		next(csvfile) # Skip reading the first line this the header
		for row in reader:
			if row["KEY"] in lookupMap:
				lookupMap[row["KEY"]].append(row["LANGUAGE"])
			else:
				lookupMap[row["KEY"]] = [row["LANGUAGE"]]
print "Done processing all files, attempting to create merged file" + "\n"

finalResult =[]
finalResult.append(finalHeader)
for key in lookupMap:
	row = []
	row.append(key)
	row.extend(lookupMap[key])
	finalResult.append(row)

# print finalResult
# print finalHeader
with open("mergedfile.csv", "wb") as resultfile:
	w = csv.writer(resultfile, delimiter=',')
	w.writerows(finalResult)

print "Merged file created. Look for mergedfile.csv on current path"
