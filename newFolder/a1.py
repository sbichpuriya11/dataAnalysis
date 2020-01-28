'''# importing csv module 
import csv 

# csv file name 
filename = "C:\\Users\\Sagar\\Downloads\\total_data_na.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting field names through first row 
	fields = csvreader.next() 

	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 

# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 

# printing first 5 rows 
print('\nFirst 5 rows are:\n') 
for row in rows[:5]: 
	# parsing each column of a row 
	for col in row: 
		print("%10s"%col), 
	print('\n') '''
'''

from pandas import DataFrame

Data = {'Tasks': [300,500,700]}
df = DataFrame(Data,columns=['Tasks'],index = ['Tasks Pending','Tasks Ongoing','Tasks Completed'])

df.plot.pie(y='Tasks',figsize=(5, 5),autopct='%1.1f%%', startangle=90)


'''



import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation 
sns.set(color_codes=True)
df = pd.read_csv("C:\\Users\\Sagar\\Downloads\\data-set.csv")
# To display the top 5 rows
df.head(5)
