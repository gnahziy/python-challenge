# importing os module 
import os
# module for reading CSV files 
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# module for creating text file 
txtpath = os.path.join('.', 'analysis', 'election_analysis.txt')

# initiate variables 
total_votes = 0
list_candidates = []
dict_candidates = {}
winner = ["",0]

# reading the csv file 
with open(csvpath) as csvfile:

    # csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row first 
    next(csvreader)

    # creating for loop to count votes
    for row in csvreader:
        total_votes += 1

        candidate = row[2]
        if candidate not in list_candidates:
            list_candidates.append(candidate)
            dict_candidates[candidate] = 0
        dict_candidates[candidate] += 1

#printing the text file 
with open(txtpath,"w") as txtfile:

    output = (
        f"Election Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------------\n"
    )

    print(output)
    txtfile.write(output)

    #printing candidate votes and percentages and winner
    for x in list_candidates:
        votes = dict_candidates.get(x)
        percent = float(votes)/float(total_votes) * 100
        
        
        if (votes > winner[1]):
            winner[1] = votes
            winner[0] = x
        output = (
            f"{x}: {percent:.3f}% ({votes})\n"
        )
        print(output)
        txtfile.write(output)

    output = (
        f"----------------------------\n"
        f"Winner: {winner[0]}\n"
        f"----------------------------\n"
    )

    print(output)
    txtfile.write(output)