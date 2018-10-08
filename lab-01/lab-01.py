import numpy as np
import pandas as pd
import csv
import os

os.getcwd()

os.chdir('E:\\TR\\sample_data')

os.getcwd()


#Numpy for array maths
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)


#Python standard working
print(x + y)

#with numpy
print(np.add(x, y))



#Python standard working
print(x + y)

#with numpy
print(np.add(x, y))

#Where numpy saves time and makes codes simple
x = np.array([[1,2],[3,4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"

print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"



#importing data from computer and other locations



newdata = pd.read_csv('E:\\Shailendra\\Personal\\TR\\sample_data\\Sample_csv_File_V1.csv')

#checking the data


#gives stats about numerical variables
checkingdata = newdata.describe()

#allows us to view first X observations
newdata.head()

#getting frequency table of a single variable
newdata['OFFERCODE_'].value_counts()



print(newdata.columns) # prints the column names


# reading a csv file with options

newdata1 = pd.read_csv('E:\\Shailendra\\Personal\\TR\\sample_data\\Sample_csv_File_V2.csv')

newdata1 = pd.read_csv('E:\\Shailendra\\Personal\\TR\\sample_data\\Sample_csv_File_V2.csv',dtype=str, delimiter='|')

newdata1.dtypes

newdata1['DateofEvaluation']=pd.to_datetime(newdata1['DateofEvaluation'], format="%m/%d/%y")
 

#Changing the data type of a variable after reading a file
newdata1.Revenue = newdata1.Revenue.astype(float)

newdata1.Revenue = newdata1.Revenue.astype(int)

newdata1.dtypes

newdata1['OFFERCODE_'].unique() # calulating the unique rows


#Group by 


newdata1.agg({'Revenue':'mean'})



print(newdata1['Revenue'].mean())

print(newdata1['Revenue'].median())

print(newdata1['OFFERCODE_'].mode())

print(newdata1['Revenue'].std())

print(newdata1['OFFERCODE_'].count())


pntl = np.percentile(newdata1['Revenue'], [10,20,30,40,50,60,70,80,90,100], axis =0)



#Defining a function

#Example 1

def greetings(name):
	"""This function greets to the person passed in as	parameter"""
	print("Hello, " + name + ". Good morning!")
    

#Calling a function

greetings("Bo")    

#Example 2

def cube(num):
	"""This function returns the cube of the entered number"""

	if num >= 0:
		return num*num*num
	else:
		return "negative"
    
cube(9)
cube(-9)

#Parameters = Information can be passed to functions as parameter.

def my_function(fname):
  print(fname + " is a Data Scientist")

my_function("Bo")
my_function("Chandan")
my_function("Shailendra")
