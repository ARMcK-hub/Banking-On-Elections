''' 
VU_DABC Python Challenge Assignment: PyPoll
Author: Andrew McKinney
Creation Date: 11/19/2019
Description: File CSV reader that analyzes election data per candidate using pandas dataframes.
'''



# import modules
import pandas as pd


# designating and reading csv file
file = 'election_data.csv'

file_df = pd.read_csv(file)

# storing header row of file
file_df_header = file_df.columns.values

# renaming columns for output table (had trouble renaming after grouped)
renames = {
    'Voter ID' : 'Candidate Votes',
    'County' : '% Votes'
}

file_df  = file_df.rename(columns=renames)

# calculating the total number of votes each candidate won by grouping candidates
file_df_grouped = file_df.groupby('Candidate').count()

# calculating the total votes cast in the poll
total_votes = file_df_grouped['Candidate Votes'].sum()

# creating % of total votes won per candidate
file_df_grouped['% Votes'] = round((file_df_grouped['% Votes']/total_votes)*100, 3)

# sorting table so that it is same as homework example
file_df_grouped = file_df_grouped.sort_values('% Votes', ascending=False)

# returning the winner of the election based on popular vote
poll_weiner = file_df_grouped[file_df_grouped['% Votes'] == file_df_grouped['% Votes'].max()].index.values


# outputs to terminal
print(f'Election Results\n-------------------------')
print(file_df_grouped)
print(f'-------------------------\nTotal Votes: {total_votes}\n-------------------------\nWinner: {poll_weiner[0]}')


# outputs to csv (tagged on total votes and election winner to the dataframe)
file_df_grouped['Total Votes'] = total_votes
file_df_grouped['Election Winner'] = poll_weiner[0]
file_df_grouped.to_csv("pypoll_output.csv", index=True, header=True)