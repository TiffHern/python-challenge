# the os module for the file path across the operating system
import os
# Module for the CSV files
import csv
csvpath = os.path.join('Resources','budget_data.csv')
print(csvpath)

#open path and retrive information into variable
with open(csvpath) as bankcsv:
     #CSV reader specifices the delimiter and variable 
    csvreader = csv.reader(bankcsv, delimiter = ',')
    csvheader= next(bankcsv)
    date = []
    revenue = []
    changes = []
    months = 0
    total_revenue = 0
    
    for row in csvreader:
        #The total number of months 
        months += 1
        #The total revenue
        total_revenue += (int(row[1]))
        date.append(row[0])
        revenue.append(row[1])

#open path and retrive information into variable
with open(csvpath) as bankcsv:
     #CSV reader specifices the delimiter and variable 
    csvreader = csv.reader(bankcsv, delimiter = ',')
    csvheader= next(bankcsv)
    totalchange = 0
    totalrowsforaverage = 0
    firstrow = next(csvreader)
    previousvalue = int(firstrow[1])
    greatestincrease = 0
    greatestdescrease = 0
    fluctuation = 0
    revenue = []
    
    
    #The total average of change between months
    for nextrow in csvreader:
        totalchange = totalchange + int(nextrow[1])- previousvalue
        totalrowsforaverage = totalrowsforaverage + 1
        previousvalue = int(nextrow[1])
        #The greatest increase in profits (date and amount) over the entire period
        #The greatest decrease in losses (date and amount) over the entire period
      
        fluctuation = totalchange + previousvalue
        revenue.append(fluctuation)
    greatestincrease = max(revenue)
    greatestdescrease = min(revenue)
        
        
print("Total Months: " + str(months))
print("Total Revenue: " + str(total_revenue))
# Subtraction/ total of rows will produve the average and round it so there is not too many decimals
print("Total Average: $" + str(round(totalchange/totalrowsforaverage)))
print("Greatest Increase: " + str(greatestincrease))
print("Greatest Decrease: " + str(greatestdescrease))
 
# Writing output to text file in folder called Analysis
writefilepath = os.path.join("Analysis", "BankAnalysis.txt")
write_file = open(writefilepath, 'w')
write_file.write("Financial Bank Analysis\n")
write_file.write("---------------------------------------------\n")
write_file.write("Total Months: " + str(months) + "\n")
write_file.write("Total Revenue: " + str(total_revenue) + "\n")
write_file.write("Total Average: $" + str(round(totalchange/totalrowsforaverage)) + "\n")
write_file.write("Greatest Increase: " + str(greatestincrease) + "\n")
write_file.write("Greatest Decrease: " + str(greatestdescrease) + "\n")
# write_file.close()