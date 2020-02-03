# Add our dependencies.
import csv
import os

# File to path
file_to_load = os.path.join("ElectionAnalysis", "election_results.csv")

# Save to path
file_to_save = os.path.joinos.path.join("ElectionAnalysis", "election_results.csv")

# Declare all variables, and set to zero.
total_votes = 0
candidate_options = []
candidate_votes = {}
county_names = []
county_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
largest_county_turnout = ""
largest_county_vote = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Increase by one for both candidates and counties  every time the loop loops, and build the candidate list
        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]

        # If the candidate isn't on the list yet add him or her
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Track the vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate’s count
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing county add to the list
        if county_name not in county_names:
            county_names.append(county_name)

            # Track the vot count for each county on the list and add a vote to the list
            county_votes[county_name] = 0
        county_votes[county_name] += 1


 #The winner of the election based on popular vote
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {candidate_percentage:.1f}%\n"
    f"-------------------------\n")

    print(winning_candidate_summary)

    txt_file.write(election_results)

    # Challenge: Save the final county vote count to the text file
    for county in county_votes:
        # Retrieve vote count and percentage
        county_vote = county_votes[county]
        county_percent = int(county_vote) / int(total_votes) * 100

        county_results = (
            f”{county}: {county_percent:.1f}% ({county_vote:,})\n”)
        print(county_results, end=“”)
        txt_file.write(county_results)

        # Determine winning vote count and candidate
        if (county_vote > largest_county_vote):
            largest_county_vote = county_vote
            largest_county_turnout = county


    txt_file.write(largest_county_turnout)

    # Save the final candidate vote count to the text file.
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (
            f”{candidate}: {vote_percentage:.1f}% ({votes:,})\n”)

        # Print each candidate’s voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

#The county with the largest turnout of voters
largest_county_turnout = (
    f"-------------------------\n"
    f"Winner: {winning_county}\n"
    f"Winning Vote Count: {winning_county_votes:,}\n"
    f"Winning Percentage: {county_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_county_turnout)
print(candidate_name)

