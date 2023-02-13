'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open("employee_data.csv", "r")

employee = csv.load(infile)

csvreader = csv.reader(infile, delimiter = (','))

#create an empty dictionary
employee_data = {}

name = ''

#use a loop to iterate through the csv file
for employee_data in csvreader:
    outfile.write(employee_data[1] + '' + employee_data[2] + '' + employee_data[5])

    #check if the employee fits the search criteria
    if name in employee_data:
        print(employee_data[1] + employee_data[5]*1.1)


    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
for employee in employee_data:
    if employee in employee_data:
        print(f"Manager Name: {employee["instnm"]})")
        print(f"Salary: {employee["name"]}")



          
     
    
infile.close()
outfile.close()
