#Import modules
import os
import csv

#Finding file in directory
election_csv =os.path.join('..', 'Resources', 'election_data.csv')

#Open and read file
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Define variables
votes = 0
candidates = []
vote_count = {}
vote_percent = {}
    
    #Vote counting & Candidates within csv
    for row in csvreader:
        
        votes = votes + 1        

        if row[2] not in candidates and row[2] not in "Candidate":
            candidates.append(row[2])
            vote_count[row[2]] = 1
        elif row[2] in candidates and row[2] not in "Candidate":
            vote_count[row[2]] = vote_count[row[2]] + 1

    #Voter percentage calculation & winner
    for item, value in vote_count.items():
        vote_percent[item] = str(round(((value/votes)*100),3)) + "% ("+str(value) + ")"
    winner = max(vote_count.items(), item=(lambda k: vote_count[k]))    
    
    #Printing format variables
    line = "-------------------------------"
    election_results = (
        "Election Results" + '\n' + line + '\n' + "Total Votes: "+ str(votes)+ '\n' + line + '\n')
    winner = (
        line + '\n'
        "Winner: "+ str(winner)+ '\n' + line + '\n')
   
   #Print Results
    print(election_results)
    for item, val in vote_percent.items():
        print(item, ": ", val)
    print(winner)
    
    #Results text file
election_file = os.path.join("Analysis", "output.txt")
with open(election_file, "w") as file:

    file.write(election_results)
    for item, val in vote_percent.items():
         f.write((item + ": " + val)+ '\n')
    file.write(winner)
    file.close()
