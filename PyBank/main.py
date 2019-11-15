''' 
VU_DABC Python Challenge Assignment: PyBank
Author: Andrew McKinney
Creation Date: 11/15/2019
Description: File CSV reader that analyzes for significant data points.
'''

# import modules
import csv as csv

# designating file
file = 'budget_data.csv'

# opening & reading file
with open(file, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')

    # initializing a header
    csv_header = next(csvreader)

    # counting rows in csv (assuming individual months)
    dates = []
    profits = []
    profit_change = []

    prev_profit = 0

    # iterating through each row in file
    for row in csvreader:
        date = row[0]
        profit = int(row[1])

        # excluding any repeat data & creating lists
        if date not in dates:
            dates.append(date)
            profits.append(profit)
            
            change = profit - prev_profit

            #exclude 1st row
            if len(dates) != 1:
                profit_change.append(change)
                
            prev_profit = profit


    # Output to terminal
    print('Financial Analysis')
    print('--------------------------------------------------')
    print(f'Total Months:  {len(dates)}')
    print(f'Total Net Profit:  ${sum(profits)}')
    print(f'Average Change:  ${round(sum(profit_change)/len(profit_change),2)}')
    print(f'Greatest Increase in Profit:  {dates[profit_change.index(max(profit_change))]} (${max(profit_change)})')
    print(f'Greatest Decreast in Profit:  {dates[profit_change.index(min(profit_change))]} (${min(profit_change)})')
    print('--------------------------------------------------')



# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# check if output file exists and up revision item # to last created
# writing output to file