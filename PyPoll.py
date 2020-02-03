#Dependencies
import csv
import os

#Assign the path
output_path = os.path.join("ElectionAnalysis", "election_results.csv")

#open CSV file, skip header row, and print headers
with open(output_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)
    print(headers)

#Preform analysis
    # Total number of votes cast
    # complete list of candidates who received votes
    total_votes = 0 
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    candidates = {}
    candidate_options = []

    for i in csvreader: 
            total_votes += 1
            candidate_name = i[2]

            if candidate_name not in candidate_options: 
                candidate_options.append(candidate_name)
                candidates[candidate_name] = 1
                print(candidate_name)
            else:
                # total number of votes each candidate received               
                candidates[candidate_name] = candidates[candidate_name] + 1
    print(total_votes)
    print(candidates)
# Percentage of votes each candidate won
for i in candidates:
        print(i)
        candidates[i]
        print(candidates[i])
        candidate_percentage = (candidates[i] / total_votes) * 100
        print(candidate_percentage)


#The winner of the election based on popular vote
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {candidate_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)

#Election Results 3.6.1
#txt_file.write(election_results)
#Output for total votes
# Close the file
#election_results.clos()
