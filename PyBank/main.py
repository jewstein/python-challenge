# PyBank data
import csv
import statistics

# Variables
tot_months = 0
nettotal_amount = 0.0
pl_change = []
great_inc = ["",0]
great_dec = ["",0]
pm_pl = 0
result = []

# Open the CSV
with open("Resources/budget_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
        #Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    for row in csvreader:

        #Add months
        tot_months = tot_months + 1

        #Add profit/loss
        nettotal_amount = nettotal_amount + int(row[1])

        #Calcualte change in PL then average
        if tot_months >1:
            pl_change.append(int(row[1]) - pm_pl)

        pm_pl = int(row[1])
        
        #Greatest increase
        if great_inc[1] < int(row[1]):
            great_inc[1] = row[0]
            great_inc[1] = int(row[1])

        #Greatest decrease
        if great_dec[1] > int(row[1]):
            great_dec[1] = row[0]
            great_dec[1] = int(row[1])

    result.append('Financial Analysis')
    result.append('......................')
    result.append(f'Total Months: ({tot_months}')
    result.append(f'Total Profit/Loss: $ {nettotal_amount}')
    result.append(f'Average Change: $ {round(statistics.mean(pl_change),2)}')
    result.append(f'Greatest Increase in Profits: $ {great_inc[1]} ')
    result.append(f'Greatest Decrease in Profits: $ {great_dec[1]} ')

    #Print
    for item in result:
        print(item)

    #Print results to "analysis" text:
    with open("analysis/results.txt", 'w') as text_file:
        text_file.write(item + "\n")



        
        

        

        
 