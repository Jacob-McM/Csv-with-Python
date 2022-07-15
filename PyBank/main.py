import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

#Lists
csv_full = []
delta_date = []

#Variables
delta_count = 0
date_count = 0
net_total = 0
profit = 0
loss = 0
average_change = int
difference = int


        #Append the csvfile into a list so that csvreader doesn't have to be acessed each time I want to get info from it

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        
    next(csvreader, None)    

    for row in csvreader:
        csv_full.append(row)

        #Date count and Total vales 

date_count = len(csv_full)  

net_total = sum(float(row[1]) for row in csv_full)


        #To get the delta of the profit/loss column starting from the 2nd position for the length of csv_full.

for n in range(1,len(csv_full)):  

    difference = (int(csv_full[n][1]))-(int(csv_full[n-1][1])) # difference = ['index' [n] in 'column' [1]] - ['index' [n-1] in column 1 ]  
     
    delta_date.append([csv_full[n][0], difference])        #delta_date is a new list that lines up the dates and delta vales to 

delta_count = len(delta_date)

change = sum(int(row[1]) for row in delta_date)/delta_count   #delta/number of changes

average_change = str(round(change, 2)) #round the change to 2 decimal places

        #a function to set the key in the max() function to so it properly iterates through the delta values in delta_date. 
def value_row(row):
    return int(row[1])

profit = max(delta_date, key = value_row)
loss = min (delta_date, key = value_row)

    
statement = (f"Financial Analysis\n" 
            f"----------------------------\n" 
            f"Total Months: {date_count}\n" 
            f"Total: ${int(net_total)}\n" 
            f"Average Change: ${average_change}\n" 
            f"Greatest Increase in Profits: {profit[0]} ${profit[1]}\n"
            f"Greatest Decrease in Profits: {loss[0]} ${loss[1]}"  )
print (statement) 

output_file = os.path.join("Analysis" , "Financial_Anaysis.txt")

with open(output_file, "w") as export:
    export.write(statement)