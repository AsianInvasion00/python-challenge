import os, csv
from pathlib import Path
file = Path("Resources", "election_data.csv")
total_votes = 0
stockham_votes = 0
degetter_votes = 0
doane_votes = 0
with open(file,newline="", encoding="utf-8") as elections:
    csv = csv.reader(elections,delimiter=",")
    header = next(csv)
    for row in csv:
         total_votes +=1
         if row[2] == "Charles Casper Stockham":
                 stockham_votes +=1
         elif row[2] == "Diana DeGette":
                 degetter_votes +=1
         elif row[2] == "Raymon Anthony Doane":
                 doane_votes +=1
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [stockham_votes, degetter_votes, doane_votes]
dic_candidates_and_votes = dict(zip(candidates,votes))
key = max(dic_candidates_and_votes, key=dic_candidates_and_votes.get)
stockham_percent = (stockham_votes/total_votes)*100
degetter_percent = (degetter_votes/total_votes)*100
doane_percent = (doane_votes/total_votes)*100
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Diana DeGette: {degetter_percent:.3f}% ({degetter_votes})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")
analysis = Path("analysis", "analysis.txt")
with open(analysis,"w") as file:
      file.write(f"Election Results")
      file.write("\n")
      file.write(f"----------------------------")
      file.write("\n")
      file.write(f"Total Votes: {total_votes}")
      file.write("\n")
      file.write(f"----------------------------")
      file.write("\n")
      file.write(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
      file.write("\n")
      file.write(f"Diana DeGette: {degetter_percent:.3f}% ({degetter_votes})")
      file.write("\n")
      file.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
      file.write("\n")
      file.write(f"----------------------------")
      file.write("\n")
      file.write(f"Winner: {key}")
      file.write("\n")
      file.write(f"----------------------------")
