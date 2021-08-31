#import dependancies 
import os 
import csv

#csvpath#
csvpath = os.path.join("Resources", "election_data.csv")
print("Election Results")
print("---------------------------------")   
#open csv 
with open(csvpath, 'r') as csvfile:
    row_list = list(csvfile)
    row_list.pop(0)
    votes = len(row_list)
    print("Total votes: " + str(votes))
print("---------------------------------") 
with open(csvpath, 'r') as csvfile:
    #initialize variables
   Candidate = ''
   line_count = 0 
   vote = 0 
   Winner = ''
   Winner_list = []
   vote_count_1 = 0 
   vote_count_2 = 0
   vote_count_3 = 0
   vote_count_4 = 0
   vote_count_1_percentage = 0
   vote_count_2_percentage = 0
   vote_count_3_percentage = 0
   vote_count_4_percentage = 0
   Candidate_list = []
   Candidate_set = []
   for line in csv.DictReader(csvfile): 
        #track lines in file
        line_count += 1
        Candidate = line["Candidate"]
        vote = line["Candidate"] 
        if Candidate not in Candidate_list: 
            Candidate_list.append(Candidate)
        if vote == Candidate_list[0]:
            vote_count_1 += 1 
        elif vote == Candidate_list[1]:
            vote_count_2 += 1
        elif vote == Candidate_list[2]:
            vote_count_3 += 1 
        else:
            vote_count_4 += 1 
        if vote_count_1 > vote_count_2 and vote_count_3 and vote_count_4:
            Winner_list.append(Candidate_list[0])
        elif vote_count_2 > vote_count_1 and vote_count_3 and vote_count_4:
            Winner_list.append(Candidate_list[1])
        elif vote_count_3 > vote_count_1 and vote_count_2 and vote_count_4:
            Winner_list.append(Candidate_list[2])
        else: 
            Winner_list.append(Candidate_list)

Winner_list = list(Winner_list)
Winner = Winner_list[0]
vote_count_1_percentage = (vote_count_1 / votes) * 100
vote_count_2_percentage = (vote_count_2 / votes) * 100
vote_count_3_percentage = (vote_count_3 / votes) * 100
vote_count_4_percentage = (vote_count_4 / votes) * 100

print(Candidate_list[0] + ": " + "{:.3f}".format(vote_count_1_percentage) + "% (" + str(vote_count_1)+ ")")
print(Candidate_list[1] + ": " + "{:.3f}".format(vote_count_2_percentage) + "% (" + str(vote_count_2)+ ")") #Correy: 20.000% (704200)
print(Candidate_list[2] + ": " + "{:.3f}".format(vote_count_3_percentage) + "% (" + str(vote_count_3)+ ")") #Li: 14.000% (492940)
print(Candidate_list[3] + ": " + "{:.3f}".format(vote_count_4_percentage) + "% (" + str(vote_count_4)+ ")") #O'Tooley: 3.000% (105630)
print("-------------------------")
print("Winner: " + str(Winner[0]))
print("-------------------------")