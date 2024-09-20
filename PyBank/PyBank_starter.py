# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# For Date manipulations
import datetime

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
greatest_inc_in_profit = 0.0
greatest_dec_in_profit = 0.0
Ave_net_change = 0.0
#month_greatest_increase = datetime.date.today()
#month_greatest_decrease = datetime.date.today()

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    row1 = next(reader)
    
    # Track the total and net change
    total_months = 1
    total_net = float(row1[1])
    new_profit_loss = float(row1[1])
    month_greatest_increase = row1[0]
    month_greatest_decrease = row1[0]
    total_change = 0
    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1

        # Track the net change
        total_net += float(row[1])
        net_change = float(row[1])- new_profit_loss
        total_change += net_change
        new_profit_loss = float(row[1])
        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_inc_in_profit :
            greatest_inc_in_profit = net_change
            month_greatest_increase = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_dec_in_profit :
            greatest_dec_in_profit = net_change
            month_greatest_decrease = row[0]

# Calculate the average net change across the months
Ave_net_change = total_change/(total_months-1)

# Generate the output summary


# Print the output
print(" Financial Analysis")
print("")
print('---------------------------------')
print("")
print("Total Months: " + str(total_months))
print("")
print("Total: $"+ str(round(total_net)))
print("")
print("Average Change: $" + str(round(Ave_net_change,2)))
print("")
print("Greatest Increase in Profits : " + str(month_greatest_increase) +" ($"+ str(round(greatest_inc_in_profit))+")")
print("")
print("Greatest decrease in Profits : " + str(month_greatest_decrease) + " ($" + str(round(greatest_dec_in_profit))+")")

#Write the results to a text file
with open(file_to_output, "w") as txt_file:
     txt_file.write(" Financial Analysis \n ")
     txt_file.write("\n")
     txt_file.write('--------------------------------- \n')
     txt_file.write("\n")
     txt_file.write("Total Month: " + str(total_months)+ "\n")
     txt_file.write("\n")
     txt_file.write("Total: $"+ str(round(total_net))+ "\n")
     txt_file.write("\n")
     txt_file.write("Average Change: $" + str(round(Ave_net_change,2))+"\n")
     txt_file.write("\n")
     txt_file.write("Greatest Increase in Profits : " + str(month_greatest_increase) +" ($"+ str(round(greatest_inc_in_profit))+") \n")
     txt_file.write("")
     txt_file.write("Greatest decrease in Profits : " + str(month_greatest_decrease) + " ($" + str(round(greatest_dec_in_profit))+") \n")
