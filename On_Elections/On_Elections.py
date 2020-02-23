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
    'Voter ID' : 'Vote Count',
    'County' : '% Votes'
}

file_df  = file_df.rename(columns=renames)

# calculating the total number of votes each candidate won by grouping candidates
file_df_grouped = file_df.groupby('Candidate').count()

# calculating the total votes cast in the poll
total_votes = file_df_grouped['Vote Count'].sum()

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


# outputs to csv
    # indicating each candidates election standing based on maximum vote count
file_df_grouped['Election Standing'] = ['Winner' if x == file_df_grouped['% Votes'].max() else 'Loser' for x in file_df_grouped['% Votes']]

    # creating total vote count series for the dataframe
total_votes_sr = pd.Series([file_df_grouped['Vote Count'].sum(), '', ''], index=file_df_grouped.columns, name='Total Votes')

    # appending the total vote count series to the dataframe
file_df_grouped = file_df_grouped.append(total_votes_sr, ignore_index=False)

    # exporting final dataframe to csv
file_df_grouped.to_csv("pypoll_output.csv", index=True, header=True)