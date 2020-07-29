import os
# Module for the CSV files
import csv
csvpath = os.path.join('Resources','election_data.csv')
print(csvpath)

#open path and retrive information into variable
with open(csvpath) as csvfile:
      #CSV reader specifices the delimiter and variable 
     csvreader = csv.reader(csvfile, delimiter = ',')
     # header = ['Voter ID','County','Candidate']
     candidates_unique=[]
     candidate_votes_amount = []
     vote_count = 0
     # election_data = ['1','2']
     nextline= next(csvreader)
     for row in csvreader:
          # Vote count
          vote_count += 1
          # Candidates List reads from the third row called 3
          candidates_list = (row[2])

          if candidates_list in candidates_unique:
               #
               candidates_index = candidates_unique.index(candidates_list)
               candidate_votes_amount[candidates_index] = candidate_votes_amount[candidates_index] + 1
          else:
               candidates_unique.append(candidates_list)
               candidate_votes_amount.append(1)

     print("Total Votes: " + str(candidate_votes_amount))
     print("Each Candidate: " + str(candidates_unique))
     print("Index: "+ str(candidates_unique.index(candidates_list)))

#  # # Writing output to text file in folder called Analysis
# writefilepath = os.path.join("Analysis", "Election_Poll_Analysis.txt")
# write_file = open(writefilepath, 'w')
# write_file.write("Election Poll Analysiss\n")
# write_file.write("---------------------------------------------\n")
# write_file.write("Total Votes " + str(months) + "\n")
# write_file.write("Total Revenue: $" + str(total_revenue) + "\n")
# write_file.write( + "\n")
# write_file.write("\n")
# write_file.write("\n")   




