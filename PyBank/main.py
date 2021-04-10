# import os module
import os

# improt module for reading csv file
import csv

# Lists to store data

months = []
total = []
profit_losses = []
idx = 0
previews_total = 0
max_month = 0
min_month = 0
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    for row in csvreader:
        print(row)
        months.append(row[0])
        total.append(int(row[1]))
        if idx == 0:
            profit_losses.append(0)
        else:
            pl = int(row[1])-previews_total
            profit_losses.append(pl)
        idx = idx+1
        previews_total = int(row[1])

    print(len(months))
    print(sum(total))
    print(sum(profit_losses)/(idx-1))
    print(max(profit_losses))
    
    max_month = profit_losses.index(max(profit_losses))
    print(months[max_month])
    min_month = profit_losses.index(min(profit_losses))
    print(months[min_month])
    print(min(profit_losses))

# --------------------------------------------------------------------------------------------------------------
# WRITE THE FINAL OUTCOME

# Set variable for output file
output_file = os.path.join('Analysis', 'pybank_outcome.txt')

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    datafile.write(f"months:{len(months)}\n")

    datafile.write(f"total:{sum(total)}\n")
    datafile.write(f"average change {sum(profit_losses)/(idx-1)}\n")
    
    max_month = profit_losses.index(max(profit_losses))
    datafile.write(f" Greatest Increase in Profits {months[max_month]} ${max(profit_losses)}\n")
    min_month = profit_losses.index(min(profit_losses))
    datafile.write(f" Greatest Decrease in Profits {months[min_month]} ${min(profit_losses)}\n")
    

