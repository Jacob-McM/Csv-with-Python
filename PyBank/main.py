import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

#Lists
profit_loss = []  #Values in 2nd column
#Variables

date_count = float
net_total = int
profit = float
loss = float
max_date = str
min_date = str
average_change = float
difference = float

        #Date counter. 

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        date_count = len(list(csvreader))
    
##print (date_count)

        #Net total counter. 

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:

        net_total = sum(float(row[1]) for row in csvreader) 

##print (net_total)       

        #Profit/Loss

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader, None)

    for row in csvreader:
        
        profit_loss.append(row[1])

        profit = max(profit_loss, key= float) 
        loss = min(profit_loss, key = float)

        if (row[1]) == profit:
            max_date = (row[0])
        
        if (row[1]) == loss:
            min_date = (row[0])
        
##print (max_date, min_date)
        

average = (int(net_total))/(int(date_count))

average_change =round(average,2)


statement = (f"Financial Analysis\n" 
            f"----------------------------\n" 
            f"Total Months: {date_count}\n" 
            f"Total: ${int(net_total)}\n" 
            f"Average Change: ${average_change}\n" 
            f"Greatest Increase in Profits: {max_date} ${profit}\n"
            f"Greatest Decrease in Profits: {min_date} ${loss}" )
print (statement) 

output_file = os.path.join("Financial_Anaysis.txt")

with open(output_file, "w") as export:
    export.write(statement)