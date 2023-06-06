# importing os module 
import os
# module for reading CSV files 
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# module for creating text file 
txtpath = os.path.join('analysis', 'budget_analysis.txt')

# Initialize variables 
total_months = 0
total_net = 0
list_month = []
list_change = []
g_increase = ["", 0]
g_decrease = ["", 99999999999999999]

# reading the csv file 
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    next(csvreader)
    
    # establish first row 
    first_row = next(csvreader)
    total_months += 1
    
    # establish previous row 
    previous = int(first_row[1])
    total_net += int(first_row[1])

    # Read each row of data after the header
    for row in csvreader:
        #find out total number of months 
        total_months += 1
        #calculate total profit 
        total_net += int(row[1])
        #calculate net change 
        net_change = int(row[1]) - previous
        previous = int(row[1])
        list_change += [net_change]
        list_month += [row[0]]

        if net_change >= g_increase[1]:
            g_increase[1] = net_change
            g_increase[0] = row[0]
        if net_change <= g_decrease[1]:
            g_decrease[1] = net_change
            g_decrease[0] = row[0]   
    #calculate total change
    total_change = sum(list_change)/len(list_change)
    
#printing the text file 
with open(txtpath,"w") as txtfile:

    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${total_change:.2f}\n"
        f"Greatest Increase in Profits: {g_increase[0]} (${g_increase[1]})\n"
        f"Greatest Dncrease in Profits: {g_decrease[0]} (${g_decrease[1]})"
    )

    print(output)
    txtfile.write(output)