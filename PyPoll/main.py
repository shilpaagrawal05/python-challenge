import os
import csv

# Declaring the variables and list 
totalvotes = 0
candidates_list = []
candidates_got_votes = []
votes= []
percentvotes = []


csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath, newline ="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    csvheader = next(csvfile)
    
    for row in csvreader:
        totalvotes += 1
        candidates_list.append(row[2])
       
   
    for candidate in candidates_list:
        if candidate not in candidates_got_votes:
            candidates_got_votes.append(candidate) 
    
    print("Election Results")
    print("------------------------------")
    print(f"Total votes : {totalvotes}")
    print("------------------------------")

    max_vote = 0

    for candidate_vote in candidates_got_votes:
        candidate_totvotes = 0
        for candidate in candidates_list:
            if candidate_vote == candidate:
                candidate_totvotes += 1
                percent_votes = (candidate_totvotes/totalvotes) * 100
                percent_votes = round(percent_votes,2)
        
        print(f"{candidate_vote}: {percent_votes}% ({candidate_totvotes})")

        votes.append(candidate_totvotes)
        percentvotes.append(percent_votes)

    max_vote = votes[0]
    winner_name = candidates_got_votes[0]

    for k in range(len(votes)):
        if votes[k] >  max_vote:
            max_vote =  votes[k]      
            winner_name = candidates_got_votes[k]
    
    
    print("------------------------------")
    print(f"Winner : {winner_name}")
    print("------------------------------")         

    

    # Writing the result to output text file
    output_path = os.path.join('Resources','output_data.txt')

    with open(output_path, 'w') as text:

        text.write("Election Results \n")
        text.write("------------------------------ \n")
        text.write("Total votes : %d \n" % totalvotes)
        text.write("------------------------------ \n")
        for i in range(len(candidates_got_votes)):
            text.write("%s%s  %.2f%s %s%d%s \n" % (candidates_got_votes[i],":",percentvotes[i],"%","(",votes[i],")"))
        text.write("------------------------------ \n")
        text.write("Winner : %s \n" % winner_name)
        text.write("------------------------------ \n")


    
    
   