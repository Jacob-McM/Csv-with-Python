#Task
### *PyBank*
>----
>In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will give a set of financial data called `[budget_data.csv]`
>>
  >>* The total number of months included in the dataset
>>
  >>* The net total amount of "Profit/Losses" over the entire period.
>>
  >>* The changes in "Profit/Losses" over the entire period, and then the average of those changes.
>>
  >>* The greatest increase in profits (date and amount) over the entire period.
>>
  >>* The greatest decrease in profits (date and amount) over the entire period
  >----
### *PyPoll*
>----
>In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
You will be given a set of poll data called `[election_data.csv]`
  >>* The total number of months included in the dataset
>>
  >>* The net total amount of "Profit/Losses" over the entire period.
>>
  >>* The changes in "Profit/Losses" over the entire period, and then the average of those changes.
>>
  >>* The greatest increase in profits (date and amount) over the entire period.
>>
  >>* The greatest decrease in profits (date and amount) over the entire period
  >----

  # Description
  
### *PyBank*

Opens the included `[budget_data.CSV]` file and appends the contents of the file without its headers to a list. The list is `[Month-Year, Profit/Loss]`. The length of that list is used to get the number of months from the budget period. From the same list, the values in `row[1]` is summed up to return the net total. The changes in profit/losses is gotten from starting on the 1st index(2nd value) of `row[1]` and subtracted from the previous index. A new list is created from these values, lined up with corresponding dates.The list is `[Month-Year, Delta]`.  The delta row is summed up and then divided by the new month-year count from this new list to get the average of delta. A max and min value is also gotten from this list, along with the corresponding dates. 

All of the collected information is printed in the terminal and printed into a .txt file.


----

### *PyPoll*
Opens the included `[Election_data.csv]` file and appends 3 lists without headers. One for the entire CSV, one for the Candidates and one for the Ballot IDs. The total votes are gotten from the length of the list containing the entire CSV. Next the list containing the candidates is cleaned up then stored into a dictionary. This dictionary is counted for each occurance of candidate from a set created from the candidate list, from which the `{Candidate: Vote Count}` dictionary is created. Using the dictionary created for the vote count, the vote count that each candidate got is divided by the total votes cast and is multiplied by 100. Those values are rounded to their 3rd decimal place. The winner is gotten from the vote count dictionary from whoever had the highest vote count. 

In the case of tie for winner as per pythons documentation on max() `"If multiple items are maximal, the function returns the first one encountered"`, therefore I added something small that at least alerts if there's a tie. `Note` this alerts to ANY tie. I couldn't figure out a way to recognize duplicate values in a dictionary that were == to the maximum vote value and add +1 to a counter for each occurence in the dictionary. The idea was that if the counter ever was >1 then the message would print. Oh well, I ran out of time so this is what stays. 

Moving on, as long as the input follows `[Election_data.csv` this seems scalable to an unknown amount of candidates. I tested this code on 3 new unique candidates, one with an additional 90 votes, one with 2000 votes and one with 272,892 votes to test a max tie. With each additional candidate the code was indifferent, so I can at least say it scales to at least 644,000 votes across 6 unique candidates. It would also seem pretty simple to pass ballotIDs through a set to eliminate any duplicate BallotIDs, although I guess that depends on your voting system. 

---
# Contents

Included in this repo are two folders, one is PyBank and one is PyPoll. 

PyBank contains
  * `(PyBank\Analysis)` containing the output analysis text file.
  * `(PyBank\Resources)` containing the `budget_date.csv`.csv that the code pulls data from
  * `(PyBank\main.py)` which is the python code that will do everything described above.
  
  PyPoll contains
  * '`(PyPoll\Analysis)` containing the output analysis text file.
  * `(PyPoll\Resources)` containing the `election_data.csv`.csv that the code pulls data from
  * `(PyPoll\main.py)` which is the python code that will do everything described above.


### Sources
##### © 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
