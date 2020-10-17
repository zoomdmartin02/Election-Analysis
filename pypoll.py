# Add our dependencies
import csv
import os

#assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#addin total vote counter variable
total_votes = 0

# candidate options and candidate votes
candidate_options = []

#declare empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do:  read and analyze data here
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    #print(headers)


    # Print each row in the CSV file.
    for row in file_reader:
        #print(row)
         # increment the vote total
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]
        
        
        # check for membership and add if not already in list
        if candidate_name not in candidate_options:
            
            # add candidate name to the candidate list
            candidate_options.append(candidate_name)

            # track the candidate's vote count
            candidate_votes[candidate_name] = 0

        # add vote to candidate
        candidate_votes[candidate_name] += 1

        # Determine the percentage of votes for each candidate by looping through the counts.
        #1.  Iterate through the candidate list

        for candidate_name in candidate_votes:
            
            #2. Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]

            #3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            #4. Print the candidate name and percentage of votes
            #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
            
            # Determine winning vote count and candidate
            # Determine if the votes is greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):

                #if true then set winning_count = votes and winning_percent = vote percentage
                winning_count = votes
                winning_percentage = vote_percentage

                #and, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

                #to do: print out each candidates
            # To do: print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")



        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)

#print the total # of votes
#print(total_votes)

#print the candidate list
#print(candidate_options)

#print the candidate vote dictionary
#print(candidate_votes)





    