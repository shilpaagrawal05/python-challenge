import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath, newline ="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    csvheader = next(csvfile)

    # Declaring the variables and list 
    totalmonths = 0
    net_tot_profitloss = 0
    totchange = 0 
    profitloss = []
    change_profloss = []
    dates = []

    # Calculate the total number of months included in the dataset
    # Calculate the net total amount of profit/loss over the entire period
    for row in csvreader:
        totalmonths += 1
        net_tot_profitloss +=  int(row[1])

        
        profitloss.append(row[1])
        dates.append(row[0])
    
    #Calculate the length of the profit/loss column
    length = len(profitloss)
   
   #Calculate the change in the profit/loss over the entire period.
    for i in range(length):
        if i < (length - 1):
            cal_change = int(profitloss[i+1]) -  int(profitloss[i])
            change_profloss.append(cal_change)
    
    # Calculate the length of the change in profit/loss list
    length_new = len(change_profloss)

    MaxProfit = change_profloss[0]
    MinProfit = change_profloss[0]
    date = dates[0]

    for j in range(length_new):
        totchange += int(change_profloss[j])
         
        if change_profloss[j] > MaxProfit:
            MaxProfit = change_profloss[j]
            date= dates[j+1]
        
        if change_profloss[j] < MinProfit:
            MinProfit = change_profloss[j]
            date1 = dates[j+1]

# Calculate the average of the changes in profitloss over the entire period.  
    avg_change = totchange / length_new
    avg_change = round(avg_change,2)

# Printing the analysis to the terminal
    print("Financial Analysis")
    print("------------------------------")
    print(f"Total months : {totalmonths}")
    print(f"Total Profit/Losses : ${net_tot_profitloss}")
    print(f"Average change : ${avg_change}")
    print(f"Greatest Increase in Profits : {date} (${MaxProfit})")
    print(f"Greatest Decrease in Profits : {date1} (${MinProfit})")


# Writing the result to output text file
    output_path = os.path.join('Resources','output_data.txt')

    with open(output_path, 'w') as text:

        text.write("Finalcial Analysis \n")
        text.write("----------------------------------- \n")
        text.write("Total months : %d \n" % totalmonths)
        text.write("Total Profit/Losses : %d \n" %net_tot_profitloss)
        text.write("Average change : $%.2f \n" %avg_change)
        text.write("Greatest Increase in Profits : %s $%d \n" %(str(date), MaxProfit))
        text.write("Greatest Decrease in Profits : %s $%d \n" %(str(date1), MinProfit))