from optparse import Values
import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

    #Dictionaries
candidate_dict = {} 
vote_count = {} #Candidate: Vote count 
per_won = {} #Candidate: percent won

    #lists

election = [] 
candidate_row = []  
candidate_list= []
ballot_row = []

    #variables
total_count = 0
max_vote = 0
dupe_count = 0 
    #Open CSV and append everything to its own list. Headers ignored. 

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  
    for row in csvreader:
        
        election.append(row)

        candidate_row.append(row[2])

        ballot_row.append(row[0])


    #Total count is just the length of the csv file since its indexed based off ballot ID. 
total_count = len(election)

#if voter_dupe != total_count:

    #Lines 46 to 54 all are to enable the counting of each candidates name in order to get the vote count. 

    #Makes an an indexed list in order of appearence for each candidate.                                                  
for n in candidate_row:     
    candidate_list.append(n)

candidate_dict = (candidate_list) #Makes candidate_list into a dictionary. 



    #turns candidate_row into a set to remove duplicates. For each n in that set, it counts it from the candidate dictionary
    #This gets the vote count, and this is put into a dictionary itself. {Candidate: Vote}
vote_count = dict((n,candidate_dict.count(n)) for n in set(candidate_row)) 


    #Creates a dictionary with {Candidate: Percent Won} from the vote count dictionary. 
per_won = {key: (value  / total_count) * 100 for key, value in vote_count.items()}

    #Rounds percentage.
for key, value in per_won.items():
    per_won[key] = round(value,3)

    #gets the winner based on vote_count dictionary.
winner = max(vote_count, key=vote_count.get)

    #Last minuted added functionality that checks for a tie. Very basic. Will return results on any tie. Still useful I think. 
if len(set(vote_count.values())) != len(vote_count.values()):
        print("There's a tie somewhere. Please check carefully.")


        #print("You have more than one winner. Please check carefully.")

#A long line of print statements to get the desired output. \
#I tried to make it look prettier in code, but this was the best I could do.\
#It's still completely functional, and scales with more candidates.\
#I just wish I could have found a way to pack it into a single variable like I did with the PyBank output. \

print ("                  ")
print ("Election Results")
print ("----------------------------")
print (f"Total Votes: {total_count}")
print ("----------------------------")
for key,value in per_won.items():
    print (f"{key}: {value}%", {vote_count.get(key)})  #This is the reason I couldn't get this output to be put nicely into a string. 
print ("----------------------------")                  #It prints nicely as seen, but trying to put it into a list only sends one line. 
print (f"Winner: {winner}")

#This is the biggest reason I'm annoyed at the multiple print line. I have to have it twice if I want the output text file. 
#At least it's lazy and I just add "file=of" to the end of each print. 

of = os.path.join("Analysis","Election Results.txt") 
with open(of, "w") as of:
    print ("Election Results" , file=of)
    print ("----------------------------", file=of)
    print (f"Total Votes: {total_count}", file=of)
    print ("----------------------------", file=of)
    for key,value in per_won.items():
        print (f"{key}: {value}%", {vote_count.get(key)}, file=of)
    print ("----------------------------", file=of)
    print (f"Winner: {winner}", file=of)

    




