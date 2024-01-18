import pandas as pd
ed=pd.read_csv("/Users/davidskaff/Downloads/python-challenge/PyPoll/Resources/election_data.csv")
print(ed)

# The total number of votes cast
total_votes = ed['Ballot ID'].count()
print(f'Total votes: {total_votes}')

# A complete list of candidates who received votes
candidates = ed['Candidate'].unique()
print(f'Candidates: {candidates}')

# The percentage of votes each candidate won & total number of votes each candidate won
for candidate in candidates:
    candidate_votes = ed[ed['Candidate'] == candidate]['Ballot ID'].count()
    percentage_votes = (candidate_votes / total_votes) * 100
    print(f'{candidate}: {percentage_votes}% ({candidate_votes} votes)')

# The winner of the election based on popular vote
winner = ed['Candidate'].value_counts().idxmax()
print(f'Winner: {winner}')

with open('election_results.txt', 'w') as file:

    # Write the total number of votes cast
    file.write(f'Total votes: {total_votes}\n')

    # Write the list of candidates who received votes
    file.write(f'Candidates: {", ".join(candidates)}\n')

    # Write the percentage of votes and total number of votes each candidate won
    for candidate in candidates:
        candidate_votes = ed[ed['Candidate'] == candidate]['Ballot ID'].count()
        percentage_votes = (candidate_votes / total_votes) * 100
        file.write(f'{candidate}: {percentage_votes}% ({candidate_votes} votes)\n')

    # Write the winner of the election based on popular vote
    file.write(f'Winner: {winner}\n')


