import os
# Module for the CSV files
import csv
csvpath = os.path.join('Resources','election_data.csv')
# print(csvpath)

#open path and retrive information into variable
with open(csvpath) as csvfile:
     #CSV reader specifices the delimiter and variable 
    
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = ['Voter ID','County','Candidate']
    nextline= next(csvreader)
    Voter ID= []
    County = []
    Candidate = []
    



