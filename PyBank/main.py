#Import modules
#Import modules
import os
import csv

#Import CSV
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#Read csv
with open(budget_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =',')
    header = next(csv_reader)

    print(f"Header: {header}")

    #Initializing empty lists for csv values 
    month_count = []
    profit = []
    change_profit = []

                      
    #Reading months data from csv
    for row in csvreader:
        month_count.append(row[0])
        profit.append(row[1]))
 
    #Calculating profit  
    for x in range(1, len(profit)):
        change_profit.append((int(profit[x])) - int(profit[x-1])))
    
    #Average profit 
    profit_avg = sum(change_profit) / len(change_profit)
    #Total months
    total_months = len(months)
    
    #Increase/Decrease Profit
increase = max(change_profit)
decrease = min(change_profit)

    #Results 

print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(sum(profit)))
print("Average Change: " + "$" + str(profit_avg))
print("Greatest Increase in Profits: " + str(months[profit_change.index(max(change_profit))+1]) + " " + "$" +str(increase))
print("Greatest Decrease in Profits: " + str(months[profit_change.index(min(change_profit))+1]) + " " + "$" + str(decrease))     


#Text file results
output = output.txt
with open(output,"w") as text:
    text.write("Financial Analysis")
    text.write("\n")
    text.write("------------------------")
    text.write("\n")
    text.write(f"Total Months: " + str(total_months)
    text.write("\n")
    text.write(f"Total: " + "$" + str(sum(profit)))
    text.write("\n")
    text.write("Average Change: " + "$" + str(profit_avg))
    text.write("\n")
    text.write("Greatest Increase in Profits: " + str(months[profit_change.index(max(change_profit))+1]) + " " + "$" +str(increase))
    text.write("\n")
    text.write("Greatest Decrease in Profits: " + str(months[profit_change.index(min(change_profit))+1]) + " " + "$" + str(decrease))
    text.close()
                
