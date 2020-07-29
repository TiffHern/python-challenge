import os
# Module for the CSV files
import csv
csvpath = os.path.join('Resources','election_data.csv')
# print(csvpath)

#open path and retrive information into variable
with open(csvpath) as csvfile:
      #CSV reader specifices the delimiter and variable 
     csvreader = csv.reader(csvfile, delimiter = ',')
     # header = ['Voter ID','County','Candidate']
     candidates_unique=[]
     candidate_votes_amount = []
     vote_count = 0
     winner= []
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
     print("Election Results")
     print("Total Votes: " + str(vote_count))
     # print("Each Candidate: " + str(candidates_unique))
     # print("Index: "+ str(candidates_unique.index(candidates_list)))

     percentage= []
     index = 0
     most_votes = candidate_votes_amount[0]

     for x in range(len(candidates_unique)): 
         
          # Multipling by 100 to get the result into a percent
          # for y in range(len(candidates_unique)):
          vote_percentage = round(candidate_votes_amount[x]/vote_count*100, 3)
          percentage.append(vote_percentage)

          print(str(candidates_unique[x]) + ": " + str(percentage[x]) + "%" + " (" + str(candidate_votes_amount[x]) + ")")
          #Finding the candidate with the greatest amount of votes and declaring a winner
          if candidate_votes_amount[x] > most_votes:
               most_votes = candidate_votes_amount[x]
               index = x
          
     winner = candidates_unique[index]
               # Writing output to text file in folder called Analysis
print("Election Winner:" + str(winner))


writefilepath = os.path.join("Analysis", "Election_Poll_Analysis.txt")
write_file = open(writefilepath, 'w')
write_file.write("Election Results\n")
write_file.write("---------------------------------------------\n")
write_file.write("Total Votes: " + str(vote_count) + "\n")
write_file.write("---------------------------------------------\n")
for x in range(len(candidates_unique)):
     write_file.write((str(candidates_unique[x]) + ": " + str(percentage[x]) + "%" + " (" + str(candidate_votes_amount[x])) + ") " + "\n")
write_file.write("Election Winner: " + str(winner) + "\n")
# write_file.write("\n")
write_file.write("----------------REPORT END----------------")   




