# import os module
import os

# improt module for reading csv file
import csv

# Lists to store data

votes = []
count_Khan = 0
count_Correy = 0
count_Li = 0
count_Tooley = 0
csvpath = os.path.join('Resources', 'election_data.csv')
winner_votes = 0

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
        elif row[2] == "Li":
            count_Li+=1
        elif row[2] == "O'Tooley":
            count_Tooley+=1

        #rowno+=1
        #if rowno == 1000:
            #break


    print(len(votes))
    print(count_Khan)
    print(count_Correy)
    print(count_Li)
    print(count_Tooley)
    

    print("Khan: "+str(round(count_Khan/len(votes)*100))+str(".000% ") + "("+str(count_Khan)+")")
    print("Correy: "+str(round(count_Correy/len(votes)*100))+str(".000% ") + "("+str(count_Correy)+")")
    print("Li: "+str(round(count_Li/len(votes)*100))+str(".000% ") + "("+str(count_Li)+")")
    print("O'Tuley: "+str(round(count_Tooley/len(votes)*100))+str(".000% ") + "("+str(count_Tooley)+")")
    
output_file = os.path.join('Analysis', 'pypoll_outcome.txt')

with open(output_file, "w", newline="") as datafile:
    datafile.write(f"Total Votes:{len(votes)}\n")
    datafile.write("Khan: "+str(round(count_Khan/len(votes)*100))+str(".000% ") + "("+str(count_Khan)+")\n")
    datafile.write("Correy: "+str(round(count_Correy/len(votes)*100))+str(".000% ") + "("+str(count_Correy)+")\n")
    datafile.write("Li: "+str(round(count_Li/len(votes)*100))+str(".000% ") + "("+str(count_Li)+")\n")
    datafile.write("O'Tuley: "+str(round(count_Tooley/len(votes)*100))+str(".000% ") + "("+str(count_Tooley)+")\n")








