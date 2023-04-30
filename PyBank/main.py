import os, csv
from pathlib import Path
file = Path("Resources","budget_data.csv")
months = []
profit = []
monthly_profit_change = []
with open(file,newline="", encoding="utf-8") as budget:
    csv = csv.reader(budget,delimiter=",")
    header = next(csv)
    for row in csv:
        months.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        monthly_profit_change.append(profit[i+1]-profit[i])
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})")

write_file = Path("analysis", "analysis.txt")
with open(write_file,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(months)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})")