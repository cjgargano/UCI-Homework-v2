import os
import csv

bookNum = ("1","2")

for books in bookNum:
	#reset values
	monthNums = 0
	totalRev = 0
	firstMonthRev = 0
	sumRevChange = 0
	revChange = 0
	rev1 = 0
	revData = {}
	avgRevChgList = []
	outputList = []
	#set path for input data
	csvPath = os.path.join("raw_data","budget_data_"+ books +".csv")
	
	#set path for output data
	dataAnalysis = os.path.join("output","budget_data_"+ books +".txt")

	with open(csvPath, 'r') as csvfile:
		
		csvReader = csv.reader(csvfile, delimiter=",")
		
		#skip headers
		next(csvReader, None)

		for row in csvReader:
			if len(avgRevChgList) == 0:
				firstMonthRev = int(row[1])
				avgRevChgList.append(row[1])
				revDate = row[0]
				revData[revDate] = firstMonthRev
			else:
				revChange = rev1 - int(row[1])
				avgRevChgList.append(revChange)
				sumRevChange = sumRevChange + revChange	
			revDate = row[0]
			revData[revDate] = revChange
			rev1 = int(row[1])
			monthNums = monthNums + 1
			totalRev = totalRev + int(row[1])
		avgRevChg = round((sumRevChange)/monthNums,2)
	#Print screen for debugging purposes
		print("======================================================================")
		print("budget_data_"+ books +".csv")
		print("======================================================================")
		print("Total Months: "+ str(monthNums))
		print("Total Revenue: $"+ str(totalRev))	
		print("Average Revenue Change: $"+str(avgRevChg))
		for revDate, revValue in revData.items():
			maxRevDate = max(revData, key=revData.get)
			minRevDate = min(revData, key=revData.get)
			print("Greatest Increase in Revenue: " + max(revData, key=revData.get) + " ($"+ str((revData[maxRevDate])) + ")")
			print("Greatest Decrease in Revenue: " + min(revData, key=revData.get) + " ($"+ str((revData[minRevDate])) + ")")
			break
		print("======================================================================")
		
		maxIncRev = max(revData, key=revData.get)
		maxIncDate = str((revData[maxRevDate]))
		maxDecRev = str((revData[minRevDate]))
		maxDecDate = min(revData, key=revData.get)
		
		csvWriter = open("budget_data_"+books+".txt", "w+")

		csvWriter.write("======================================================================\n")
		csvWriter.write("budget_data_"+ books +".csv\n")
		csvWriter.write("======================================================================\n")
		csvWriter.write("Total Months: "+ str(monthNums))
		csvWriter.write("\nTotal Revenue: $"+ str(totalRev))	
		csvWriter.write("\nAverage Revenue Change: $"+str(avgRevChg))
		for revDate, revValue in revData.items():
			maxRevDate = max(revData, key=revData.get)
			minRevDate = min(revData, key=revData.get)
			csvWriter.write("\nGreatest Increase in Revenue: " + max(revData, key=revData.get) + " ($"+ str((revData[maxRevDate])) + ")")
			csvWriter.write("\nGreatest Decrease in Revenue: " + min(revData, key=revData.get) + " ($"+ str((revData[minRevDate])) + ")")
			break
		csvWriter.write("\n======================================================================")
		
		csvWriter.close()
