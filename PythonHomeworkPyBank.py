
# coding: utf-8

# In[101]:


import os
csvpath = os.path.join('raw_data', 'budget_data_1.csv')


import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
# initializing variables
        count = 0
        total_rev=0
        GIRev = 0
        DIRev = 0
        Rev_Curr=0
        Rev_chg=0
        GImonth='Oct-12'
        DImonth='Oct-12'
# removing header 
        next(csvreader,None)
    #  Each row is read as a row
        for row in csvreader:
#             print(row)
            count = count+1
            total_rev=total_rev+int(row[1])
        #Gratest Increase in Revenue 
            Rev_Prev=Rev_Curr
            Rev_chg_prev=GIRev
            Rev_Curr=int(row[1])
            Rev_chg=Rev_Curr-Rev_Prev
#             GIrev=Rev_chg
            if Rev_chg > GIRev :
                GIRev = Rev_chg
                GImonth=row[0]
            if Rev_chg < DIRev :
                DIRev = Rev_chg
                DImonth=row[0]
#             print(Rev_Prev,Rev_Curr, Rev_chg_prev,Rev_chg,GIRev,GImonth,DIRev,DImonth)
#         print(GIRev)
            
   
print("Financial Analysis")
print("----------------------------")
print("Total Months:", count)
print("Total Revenue:", total_rev)
print("Average Revenue Change: $",int(total_rev/count))
print("Greatest Increase in Revenue:" +str(GImonth)+ " ($"+str(GIRev) +")")
print("Greatest Decrease in Revenue:" +str(DImonth)+ " ($"+str(DIRev)+")")

