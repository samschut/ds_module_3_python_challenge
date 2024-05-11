import os
import csv

CSV_PATH = "Resources/election_data.csv"


# Open the CSV using the UTF-8 encoding

os.chdir(os.path.dirname(os.path.realpath(__file__)))


#Variables
candidate_list = []
total_id_count = 0
last_id = 0
candidate = ""
candidate_votes = {}

#open the data file in order to run the analysis
with open(CSV_PATH, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
       
    for row in csvreader:
        # THE TOTAL NUMBER OF BALLOTS
        #also, the number of votes per candidate in the same for loop
        total_id_count += 1
        candidate = row[2]
        if candidate not in candidate_list:
           candidate_list.append(candidate)
           candidate_votes[candidate] = 0
        candidate_votes[candidate] = candidate_votes[candidate] + 1
        # get the count of the rows
        if (total_id_count == 1):
        # define what last row is
            last_id = int(row[0])

        #get the count by comparing last row to what was defined as first row
        else:
            count = int(row[0]) - last_id
    print(total_id_count)
   
   
   #new candidate in order to get the percentage of the votes per candidate compared to the total votes
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        candidate_perc = float(votes) / float(total_id_count) * 100
        # print(f"{candidate}: {candidate_perc:.3f}% {votes}\n")
     
     # get the winner of the vote, xpert helped with this
      # Initialize variables to keep track of the winning candidate and their votes
winning_candidate = ""
winning_votes = 0

for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    candidate_perc = float(votes) / float(total_id_count) * 100

#Check if the current candidate has more votes than the current winning candidate
    if votes > winning_votes:
        winning_candidate = candidate
        winning_votes = votes

    print(f"{candidate}: {candidate_perc:.3f}% ({votes})")

# Print the winner
print(f"Winner: {winning_candidate}")   
        
# Define the election results
election_results = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_id_count}",
    "-------------------------"
]

# Loop through the candidate votes and percentages
for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    candidate_perc = float(votes) / float(total_id_count) * 100
    election_results.append(f"{candidate}: {candidate_perc:.3f}% ({votes})")

# Determine the winner
winning_candidate = max(candidate_votes, key=candidate_votes.get)
election_results.append("-------------------------")
election_results.append(f"Winner: {winning_candidate}")
election_results.append("-------------------------")

# Write the election results to a text file
with open("election_results_schutz.txt", "w") as file:
    for line in election_results:
        file.write(line + "\n")


