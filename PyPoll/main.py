# -*- coding: UTF-8 -*-
"""PyPoll final File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_result.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
index = 0

# Define lists and dictionaries to track candidate names and vote counts
list_candidate_name = []
list_candidate_vote = []
dict_candidate_votes = {}
# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if (candidate_name not in list_candidate_name):
            list_candidate_name.append(candidate_name)
            dict_candidate_votes.update({candidate_name : 0})
        # Add a vote to the candidate's count
        dict_candidate_votes[candidate_name] += 1
          

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(" ")
    print("Election Results ")
    print(" ")
    print("-------------------------")
    print(" ")
    print("Total Votes:" + str(total_votes))
    print(" ")
    print("-------------------------")
    print(" ")

    # Write the total vote count to the text file
   
    txt_file.write("\n ")
    txt_file.write("Election Results \n ")
    txt_file.write("\n ")
    txt_file.write("-------------------------\n")
    txt_file.write("\n ")
    txt_file.write("Total Votes:" + str(total_votes) +"\n")
    txt_file.write("\n ")
    txt_file.write("-------------------------\n")
    txt_file.write("\n ")

    # Initialise valriables to store winning candidate and winning candidate vote

    winning_candidate = list_candidate_name[0]
    winning_candidate_vote = dict_candidate_votes[winning_candidate]
    
    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in list_candidate_name :

        # Get the vote count and calculate the percentage
        candidate_vote = dict_candidate_votes[candidate]
        candidate_percent = (candidate_vote/total_votes)*100
        # Update the winning candidate if this one has more votes
        if (candidate_vote > winning_candidate_vote) :
            winning_candidate_vote = candidate_vote 
            winning_candidate = candidate
        # Print and save each candidate's vote count and percentage
        #print(" ")
        print(candidate + ": "+ str(round(candidate_percent,3))+ "% (" + str(candidate_vote) + ")")
        print(" ")

        # Write each candidate's vote count and percentage to the text file
        txt_file.write(candidate + ": "+ str(round(candidate_percent,3))+ "% (" + str(candidate_vote) + ")\n")
        txt_file.write("\n ")

    # Generate and print the winning candidate summary

    print("-------------------------")
    print("")
    print("Winner: " + winning_candidate)
    print("")
    print("-------------------------")



    # Save the winning candidate summary to the text file
    txt_file.write("-------------------------\n")
    txt_file.write("\n")
    txt_file.write(" Winner: " + winning_candidate + "\n")
    txt_file.write(" \n")
    txt_file.write(" -------------------------\n")