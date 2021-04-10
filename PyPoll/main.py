# import os module
import os

# improt module for reading csv file
import csv

# Lists to store data

votes = []

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    for row in csvreader:
        print(row)
        votes.append(int(row[0]))
    
    print(len(votes))




