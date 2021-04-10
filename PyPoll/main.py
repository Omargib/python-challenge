# import os module
import os

# improt module for reading csv file
import csv

# Lists to store data

votes = []
count_Khan = 0
count_Correy = 0
Li = []
count_Tooley = 0
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    rowno=1
    
    for row in csvreader:
        print(row)
        votes.append(int(row[0]))
        if row[2] == "Khan":
            count_Khan+=1 
        elif row[2] == "Correy":
            count_Correy+=1

        elif row[2] == "O'Tooley":
            count_Tooley+=1

        rowno+=1
        if rowno == 100:
            break


    print(len(votes))
    print(count_Khan)
    print(count_Correy)
    print(count_Tooley)
    print("Khan: "+str(round(count_Khan/len(votes)*100)))





