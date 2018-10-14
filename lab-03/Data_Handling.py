

import numpy as np
import pandas as pd
import csv
import os
from pandasql import sqldf

os.getcwd()

os.chdir('E:\\Shailendra\\Personal\\TR\\sample_data')

os.getcwd()



newdata1 = pd.read_csv('E:\\Shailendra\\Personal\\TR\\sample_data\\Sample_csv_File_V2.csv',dtype=str, delimiter='|')

newdata1.dtypes

newdata1['DateofEvaluation']=pd.to_datetime(newdata1['DateofEvaluation'], format="%m/%d/%y")
 

#Changing the data type of a variable after reading a file
newdata1.Revenue = newdata1.Revenue.astype(float)




#reordering columns
newdata1.columns = ['Revenue','PERSONID', 'CUSTID', 'ACCOUNTID', 'PROGRAMEID', 'TRFRID', 'TRFRNAME', 'TRFRDESC', 'PASSED', 'DateofEvaluation']


age = pd.read_csv('E:\\Shailendra\\Personal\\TR\\sample_data\\Sample_Age.csv',dtype=str, delimiter=',')


#Merging files
newdata2 = pd.merge(newdata1,age, how='left', on='PERSONID' ) 

newdata2.describe()

#Changing the data type of a variable after reading a file
newdata2.Age = newdata2.Age.astype(float)



#Selecting a few columns from a dataframe

t=newdata2[['PERSONID', 'PROGRAMEID', 'ACCOUNTID']]


#Creating a new variable

newdata2['rev2'] = newdata2['Revenue']*2

newdata2['rev3'] = newdata2['Revenue'] + newdata2['rev2']


#filtering data

t= newdata2[newdata2['Revenue'] > 150]



# Creating a flag variable

#newdata1.dtypes

#newdata1['Revenue'] = pd.to_numeric(newdata1['Revenue'], errors='coerce')

newdata2['Rev_flag'] = np.where(newdata2['Revenue'] > 110, 'GT_110', '<=110')


# Dropping a column


t = newdata2.drop('rev3', axis = 1)



#excluding rows based on a condition


t = newdata2[newdata2.ACCOUNTID != 'CM-DP']

t = newdata2.drop([0, 1])

#renaming a column

newdata2.rename(columns={'rev2':'total_bill'}, inplace = True)

#sorting a dataset

newdata2 = newdata2.sort_values(['total_bill', 'CUSTID_x'])



#length of string
newdata2['ACCOUNTID'].str.len().head()

#Finding a character within a string
newdata2['ACCOUNTID'].str.find("PE").head(3)

#substring from a string

newdata2['ACCOUNTID'].str[0:2].head()

#Splitting a string and using position to create a new variable

newdata2['NEWtrfrname'] = newdata2['TRFRNAME'].str.split(" ", expand=True)[1] #Expand the splitted strings into separate columns.
       


# Upcase

newdata2['TRFRNAME1'] = newdata2['TRFRNAME'].str.upper()


# Lowercase
t['TRFRNAME2']= newdata2['TRFRNAME1'].str.lower()

#Missing value treatment

newdata2['Age'].fillna(0, inplace = True)

#groupby

Rev_summed = newdata2.groupby(['ACCOUNTID', 'PROGRAMEID'])['Revenue', 'Age'].sum()



#Writing a file to external location as csv
df_test.to_csv("df_test.csv")
  



#creating multiple flags using lambda function

newdata2['age_grp'] = newdata2['Age'].apply(lambda x : 'GRP_LE_35' if x <= 35 else 'GRP_LE_50' if x > 35 and x <= 50 else 'GRP_GT_50' if x > 50 and x <= 173 else 'MISS')



#Using SQL in python

from pandasql import *
pysqldf = lambda r: sqldf(r, globals())

r= """
  Select 
  (sum(Revenue))/1000 as rev_sum000
  from newdata2
  """
  
df_test = pysqldf(r)


from pandasql import *
pysqldf = lambda r: sqldf(r, globals())

r= """
  Select 
  ACCOUNTID,
  (sum(Revenue))/1000 as rev_sum000
  from newdata2
  group by ACCOUNTID
  
  """
  
df_test = pysqldf(r)
  


from pandasql import *
pysqldf = lambda r: sqldf(r, globals())

r= """
  Select 
  ACCOUNTID,
  (sum(Revenue))/1000 as rev_sum000,
  sum(Age) as mean_age
  from newdata2
  group by ACCOUNTID
  
  """
  
df_test = pysqldf(r)
  


#Creating a band variable by using SQL
from pandasql import sqldf


from pandasql import *
pysqldf = lambda r: sqldf(r, globals())

r= """
Select *,
CASE When "Revenue" > 150 THEN ">150"
WHEN "Revenue" > 110 THEN ">110"
ELSE "<=110"
END
as "REVBand"
from newdata2
"""
df_test=pysqldf(r)
  


#functions for calculations


def func(x):
    d = {}
    d['count_cust'] = x['PERSONID'].count()
    d['total_age'] = x['Age'].sum()
    
    return pd.Series(d, index=['count_cust',
                                'total_age'])
t = newdata2.groupby(['ACCOUNTID']).apply(func).reset_index()



#----------------------------------

"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
"""


#Data visualization


#PLots
import matplotlib

from matplotlib import pyplot as plt

#plotting a simple line
plt.plot([1,2,3,4])

plt.plot([0.1, 0.2, 0.3, 0.4], [1, 2, 3, 4])

#plotting multiple lines
plt.plot([0.1, 0.2, 0.3, 0.4], [1, 2, 3, 4],
             [0.1, 0.2, 0.3, 0.4], [1, 4, 9, 16])


# Simple Line Graph
plt.plot(df_test['ACCOUNTID'], df_test['rev_sum000'] )
plt.xlabel("ACCOUNTID")
plt.ylabel("rev_sum000")



plt.plot(df_test['ACCOUNTID'], df_test['rev_sum000'],  
         df_test['ACCOUNTID'], df_test['mean_age'] )
plt.xlabel("ACCOUNTID")
plt.ylabel("Rev & Age")








#Simple Bar graph
plt.bar(df_test['ACCOUNTID'], df_test['rev_sum000'])

plt.bar(df_test['ACCOUNTID'], df_test['rev_sum000'], width = 0.1)

