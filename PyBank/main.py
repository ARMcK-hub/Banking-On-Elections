''' 
VU_DABC Python Challenge Assignment: PyBank
Author: Andrew McKinney
Creation Date: 11/15/2019
Description: File CSV reader that analyzes for significant data points.
'''



# important modules
import csv as csv

read_file = 'budget_data.csv'

# opening & reading file
with open(read_file, 'r') as read_file:
    csvreader = csv.reader(read_file, delimiter = ',')

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

            #exclude 1st row in profit change list
            if len(dates) != 1:
                profit_change.append(change)
                
            prev_profit = profit


# storing output items in list (output)
output_items = []

output_items.append(f'Financial Analysis\n--------------------------------------------------\nTotal Months:  {len(dates)}\nTotal Net Profit:  ${sum(profits)}\nAverage Change:  ${round(sum(profit_change)/len(profit_change),2)}\nGreatest Increase in Profit:  {dates[profit_change.index(max(profit_change))]} (${max(profit_change)}\nGreatest Decreast in Profit:  {dates[profit_change.index(min(profit_change))]} (${min(profit_change)}))\n--------------------------------------------------')


# printing output items to terminal
for items in output_items:
    print(items)

# check if output file exists and up revision item # to last created

# writing output to file
write_file = 'PyBank_output.csv'

with open(write_file, 'w') as write_file:
    csvwriter = csv.writer(write_file)
    
    for items in output_items:
         csvwriter.writerow(items)





# # I used the following to confirm that the print-out of the output file would be the same as the input, even though every character is delimited.
# with open('PyBank_output.csv', 'r') as csv_file:
#     csvreader = csv.reader(csv_file)
    
#     for items in output_items:
#         print(items)