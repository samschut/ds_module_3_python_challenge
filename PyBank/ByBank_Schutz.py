import os
import csv

CSV_PATH = "Resources/budget_data.csv"


# Open the CSV using the UTF-8 encoding

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# variables
month_count = 0
total_profit = 0

last_month_profit = 0
changes = []
month_changes = []

with open(CSV_PATH, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
       
    # Read each row of data after the header
    for row_data in csvreader:
        # print(row_data)    
        
        # count months
        month_count = month_count + 1
        #add profit
        total_profit = total_profit + int(row_data[1])

        # last month profit 
        # subtract this month - last month profit
        # append change to list

        #if first row, there is no change
        if (month_count == 1):
            #by definition, this is first row
            #no change since there is nothing to subtract from
            last_month_profit = int(row_data[1])
        else:
            change = int(row_data[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row_data[0])

            #reset last month profit
            last_month_profit = int(row_data[1])

    print(month_count)
    print(total_profit)
    

    #average the changes in row_data
    avg_change = sum(changes) / len(changes)
    print(avg_change)

    # find the max and associate with month in that row
    big_change = max(changes) 
    big_month_index = changes.index(big_change)
    big_month = month_changes[big_month_index]

    print(big_change)
    print(big_month)

    #find the min and associate with month in that row
    small_change = min(changes)
    small_month_index = changes.index(small_change)
    small_month = month_changes[small_month_index]

    print(small_change)
    print(small_month)


#create the text file
txt_file_out = f"""Financial Analysis
----------------------------
Total Months: {month_count}
Total: ${total_profit}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {big_month} ${big_change}
Greatest Decrease in Profits: {small_month} ${small_change}"""
#make sure it works
print(txt_file_out)
#open and save text file
with(open("txt_schutz_bybank.txt", 'w') as f):
        f.write(txt_file_out)