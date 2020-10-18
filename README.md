# Election-Analysis
---
##Overview of Election Audit
---
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.
---
1.  Calculate the total number of votes cast.
2.  Get a complete list of candidates who received votes.
3.  Calculate the total number of votes each candidate received.
4.  Calculate the percentage of votes won by each candidate.
5.  Determine the winner of the election based on popular vote.
---
## Technology Involved
---
Python is utilized to read and external .csv file, iterate through the 300,000+ lines of data and determine which candidates in an election received how many votes and at what percentage of the total votes.  In addition, votes are counted by county, percentages determined and the county with the most votes is identified.  Python functions such as CSV to read a .csv file, already mentioned and OS to read and write files and perform path joins are leveraged.
---
## Resources
---
* Data Source:  election_results.csv
* Software:  Python 3.7.6; Visual Studio Code 1.50.1
---
## Summary
---
The analysis of the election show the following:
 
### Election Audit Summary

**Total Votes: 369,711**

* Jefferson: 10.5% (38,855)
* Denver: 82.8% (306,055)
* Arapahoe: 6.7% (24,801)

**Largest County Turnout:  Denver**

**Candidate Vote and Percentage of Total Votes**
* Charles Casper Stockham: 23.0% (85,213)
* Diana DeGette: 73.8% (272,892)
* Raymon Anthony Doane: 3.1% (11,606)

**The Winner: Diana DeGette**
**Winning Vote Count: 272,892**
**Winning Percentage: 73.8%**

## Conclusion
---
The Colorado election commission that explores may leverage the code for any election going forward.  Possible ways to enhance or incorporate additional capabilities of this script could include:
* checking the ballot ids to determine if there are any duplicates, which might indicate election anomalies that should be investigated.
* future election data could be appended and with adding an election year column, comparisons between elections could occur to compare rates of participation by county, comparative vote tallies and if any of the candidates repeat their participation, comparatives on their performance could be provided.
