import numpy as np
import pandas as pd
import csv
import os

data_dir = 'C:\\Users\\gauri\\Desktop\\data-science-tutorials\\datascience-tutorials\\datasets'

#sample_file_1 =  '\\Exercise_Part_1.csv'
sample_csv_v1 = os.path.join(data_dir, 'Exercise_Part_1.csv')
sample_csv_v2 = os.path.join(data_dir, 'Exercise_Part_2.csv')
"""os.getcwd()

os.chdir(data_dir)

os.getcwd()"""

os.chdir(data_dir)

#Numpy for array maths
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)


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



newdata = pd.read_csv(sample_csv_v1)

#checking the data


#gives stats about numerical variables
checkingdata = newdata.describe()
print(checkingdata)

#allows us to view first X observations
print(newdata.head())

#getting frequency table of a single variable
newdata['age'].value_counts()



print(newdata.columns) # prints the column names


# reading a csv file with options

newdata1 = pd.read_csv(sample_csv_v1)

newdata1 = pd.read_csv(sample_csv_v1,dtype=str)

print(newdata1.dtypes)

#newdata1['DateofEvaluation']=pd.to_datetime(newdata1['DateofEvaluation'], format="%m/%d/%y")
newdata1.info()
''
#Changing the data type of a variable after reading a file
newdata1.duration = newdata1.duration.astype(float)

newdata1.duration = newdata1.duration.astype(int)

print(newdata1.dtypes)


newdata1['duration'].unique() # calulating the unique rows


#Group by 


newdata1.agg({'duration':'mean'})



print("The mean for the column is",newdata1['duration'].mean())

print("The median for the column is",newdata1['duration'].median())

print("The mode for the column is",newdata1['duration'].mode())

print("The standard deviation for the column is",newdata1['duration'].std())

print("The count for the column is",newdata1['duration'].count())


pntl = np.percentile(newdata1['duration'], [10,20,30,40,50,60,70,80,90,100], axis =0)
print('The pntl is', pntl)


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

#Example 3
def sum(a,b):
	"""this fuction returns the sum of two numbers"""
	print("The sum of two numbers is:",a + b)
	
sum(9,18)

#Example 4
def reversed_list(list):
	return list[::-1]

my_list = [3,5,6,7,8,43,26,6,99]
reverse_list= reversed_list(my_list)
print(reverse_list)

#Example 5
def mean(a,b,c,d,e):
	print("The mean for the numbers are",a+b+c+d+e/5)

mean(2,5,7,8,4)