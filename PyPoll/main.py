import csv
from os import linesep
import statistics

#Variables
can_list = []
tot_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

result = []

# #Percent of votes formula
# def percent(x):
#     num = x/total_votes
#     percentage = "{:.2%}".format(num)
#     return(percentage)

def percent(Khan_votes):
    num = Khan_votes/tot_votes
    percentage = "{:.2%}".format(num)
    return(percentage)

def percent(Correy_votes):
    num = Correy_votes/tot_votes
    percentage = "{:.2%}".format(num)
    return(percentage)

def percent(Li_votes):
    num = Li_votes/tot_votes
    percentage = "{:.2%}".format(num)
    return(percentage)

def percent(OTooley_votes):
    num = OTooley_votes/tot_votes
    percentage = "{:.2%}".format(num)
    return(percentage)




with open("Resources/election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        #Add months
        tot_votes = tot_votes + 1

        can_name = row[2]

        if row[2] in can_list:
            # add 1 to vote count
            can_votes[can_name] += 1

        else
            # add name to list
            can_list.append(can_name)
            can_votes[can_name] = 1

        
            


    

    result.append('Election Results')
    result.append('----------------------')
    result.append(f'Total Votes: ({tot_votes})')
    result.append('----------------------')
    result.append(f'Khan: ({percent(Khan_votes)} {Khan_votes})')
    result.append(f'Correy: ({percent(Correy_votes)} {Correy_votes})')
    result.append(f'Li: ({percent(Li_votes)} {Li_votes})')
    result.append(f"'O'Tooley': ({percent(OTooley_votes)} {OTooley_votes})")
    result.append('----------------------')
    result.append(f'Winner: ( )')
    result.append('----------------------')
    

    #Print results to "analysis" text:
    with open("analysis/results.txt", 'w') as text_file:
        for item in result:
            print(item)
            text_file.write(item + "\n")
