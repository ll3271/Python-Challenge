import os

import csv

csvpath = os.path.join('Resources/budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csv_reader = csv.reader(csvfile,delimiter=',')
   
    next(csv_reader)

    total_count = 0

    net_profit = 0

    total_profit_change = 0

    previous_profit = 0

    max_profit_change = -float("inf")

    min_profit_change = float('inf')

    max_profit_change_month = ""

    min_profit_change_month = ''

    for line in csv_reader:

        current_profit = float(line[1])

        current_date = line[0]

        total_count = total_count + 1 

        net_profit = net_profit + current_profit
        
        if total_count == 1:

            previous_profit = current_profit
        
            continue

        current_profit_change = current_profit - previous_profit

        if current_profit_change > max_profit_change:

            max_profit_change = current_profit_change

            max_profit_change_month = current_date

        if current_profit_change < min_profit_change:

            min_profit_change = current_profit_change

            min_profit_change_month = current_date

        total_profit_change = total_profit_change + current_profit_change

        # reset

        previous_profit = current_profit

    average_profit_change = total_profit_change / (total_count -1)


    print("Financial Analysis ----------------------------") 

    print("Total Months" + str(total_count))

    print("Total" + str(net_profit))

    print("Average Change:" + str(average_profit_change))

    print("Greatest Decrease in Profits:" + str(min_profit_change_month) +  ":" + str(min_profit_change))
    
    print("Greatest Increase in Profits:" + str(max_profit_change_month) + ":" + str(max_profit_change))
    
with open("PyBank_Results", "w") as txt_file:

    Total_month = (f"\n\nFinancial Analysis\n"
        f"-------------------------\n"
        f"Total Months: {total_count}\n")

    txt_file.write(Total_month)

    Total_ = (
        f"Total : {total_profit_change}\n") 

    txt_file.write(Total_)
    
    Average = (
        f"Average Change : {average_profit_change}\n") 

    txt_file.write(Average)
    
    biggest_increase = (
        f"Greatest Increase in Profits : {max_profit_change_month} {max_profit_change}\n" ) 
    
    txt_file.write(biggest_increase)

    biggest_decrease = (
        f"Greatest Decrease in Profits : {min_profit_change_month} {min_profit_change}\n" ) 

    txt_file.write(biggest_decrease)
    
