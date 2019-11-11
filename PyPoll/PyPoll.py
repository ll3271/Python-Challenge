import os

import csv

csvpath = os.path.join('Resources/election_data.csv')

with open(csvpath, newline='') as csvfile:

    csv_reader = csv.reader(csvfile,delimiter=',')
   
    next(csv_reader)

    vote_count = {}   

    total_number = 0

    for line in csv_reader: 

        name = line[2]

        total_number = total_number + 1

        if name in vote_count:

            vote_count[name] = vote_count[name] + 1

        else:

            vote_count[name] = 1 
    
    winner = ""

    winner_vote = 0

    for name in vote_count:

        if winner_vote < vote_count[name]:

                    winner_vote = vote_count[name]

                    winner = name


with open("Results", "w") as txt_file:

    election_results = (f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_number}\n"
        f"-------------------------\n")
    
    print(election_results)

    txt_file.write(election_results)

    for name in vote_count:

       vote_percentage = vote_count[name]/total_number* 100       

       vote_output = f"{name}: {vote_percentage:.3f}% ({total_number})\n"
       
       print(vote_output)

       txt_file.write(vote_output)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)


