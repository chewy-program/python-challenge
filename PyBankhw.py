#import dependancies 
import os 
import csv 

#csvpath#
csvpath = os.path.join("Resources", "budget_data.csv")
print("Financial Analysis")
print("---------------------------------")   
#open csv 
with open(csvpath, 'r') as csvfile:
    row_list = list(csvfile)
    row_list.pop(0)
    months = len(row_list)
    print("Total Months: " + str(months))
    profit_loss_sum = 0 
    
#sum all profit/loss in the csv file 
with open(csvpath, 'r') as csvfile:
    #initialize variables
    line_count = 0 
    previous_profit_loss = 0
    profit_loss_sum = 0 
    profit_loss = 0 
    change = 0 
    current_largest_increase = 0 
    date_of_largest_increase = ""
    current_largest_decrease = 0 
    date_of_largest_decrease = ""
    change_list = []
    
    for line in csv.DictReader(csvfile): 
        #track lines in file
        line_count += 1
        #grab previous profit_loss for change calc
        previous_profit_loss = profit_loss
        #get profit/losses from csv
        profit_loss = int(line['Profit/Losses'])
        #sum of all profit_loss
        profit_loss_sum += profit_loss
        #calculate change for all profit/losses
        change = profit_loss - previous_profit_loss
        #ignore first line in csv 
        if line_count > 1:
            #add to change list 
            change_list.append(change)
        #check if this is the largest change 
        if change > current_largest_increase: 
            #store largest change date and value 
            current_largest_increase = change
            date_of_largest_increase = str(line['Date'])
        #check if this is the largest change 
        if change < current_largest_decrease: 
            #store largest change date and value 
            current_largest_decrease = change
            date_of_largest_decrease = str(line['Date'])
       
    print("Total $" + str(profit_loss_sum))
    #sum of all changes in change list 
    change_sum = sum(change_list)
    #average of all changes 
    change_average = change_sum / len(change_list)
    #format to 2 decimal places
    formatted_change_average = "{:.2f}".format(change_average)
    print("Average  Change: $" + formatted_change_average) 
    print("Greatest Increase in Profits: " + date_of_largest_increase + " ($" + str(current_largest_increase) + ")" )
    print("Greatest Decrease in Profits: " + date_of_largest_decrease + " ($" + str(current_largest_decrease) + ")" ) 