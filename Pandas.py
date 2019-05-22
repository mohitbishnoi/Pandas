# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 10:13:26 2019

@author: Mohit
"""

import pandas as pd
import numpy as np

# panda pockage is used for genral purpose task,
# it can work with character as well as numeric values
# Mostly for table data we use panda package
# Reason - table can contain numeric column and character columns

# Series - it is a vector like object, which can store multiple vector in one diamension

series = pd.Series([10,20,30,40,50])
print(series.dtype)
print(type(series))
print(series)

# Dataframe - it is two diamensional array to store multiple value
# value can be of same type or disimilar types. But you have to keep
# same type of value for column
# most important - each column should have equal number of values
# terminology - index,observation,columns-variable


data=pd.DataFrame({'A':['A','B','C','D','E'],
                   'B':series})
print(data)

print(data.shape)
print(data.columns)
print(type(data))

#Broadcasting
data2=pd.DataFrame({'id':series,
                    'name':"Mohit"})
print(data2)

#No Broadcasting
data3=pd.DataFrame({'id':series,
                    'name':"Mohit"})
print(data3)

data4=pd.DataFrame({'A':np.arange(10),
                    'B':['BLR','CHN']*5})

len(np.arange(10))

range(10)
print(data4)

data5=pd.DataFrame({'A':np.arange(9),
                    'B':['BLR','CHN','MUM']*3})

print(data5)

data6 = pd.DataFrame(np.random.randn(10,4),columns=list("ABCD"))
print(data6)

#Extraction
data6['A'] # Extract all values of column A
data6[0:2] # it will return first 2 rows
data6['A'][0:2] # it will return first two records of colunn A


# Extract first two rows of column A and column B
data6.iloc[0:2,0:2] #iloc[rowindex,colindex]

# Extract last two rows of columns
data6.tail(2) #tail(n)- return n rows from bottom
#head(n) - return n rows from top

data6.describe() # return summary of data, give 8 different descriptive
                # statistics for each numeric columns
                # count - count of values
                # mean - average value
                # std - average deviation from mean
                # min - minimum value
                # 25% - 25% quantile value
                # 50% - 50% quantile value
                # 75% - 75% quantile value
                # max - maximum value

employee = pd.DataFrame({
        'id':pd.Series(['A101','A102','A103','A104','A105']),
        'Name':pd.Series(['D','E','F','G','H']),
        'Age':pd.Series([20,22,24,26,28]),
        'Amt':pd.Series([123,345,456,567,678])
        })

print(employee)

#Extract all names
employee['Name']
# Extract all name and age
employee[['Name','Age']]
#  Extract name of age E
employee['Age'][employee['Name']=="E"]
# Extract Amt above 500
employee[employee['Amt']>500]

#Manipulation
# Adding new columns - add new columns tax as 18% of amt
employee['tax']=(18/100)*employee['Amt']
print(employee)

# drop column        - drop age column
employee=employee.drop('Age',axis=1)

# Sorting            - sort dataframe in descending order of Amt
employee.sort_values('Amt',ascending=False)


# Add new column Sex with "F"*3 and "M"*2
employee['Sex']=['F','F','F','M','M']
employee['Sex']=['F']*3+['M']*2


# bygroup calculation - find total amt of each sex group
employee.groupby(by='Sex')['Amt'].sum()
employee.groupby(by='Sex')['Amt'].mean()
employee.groupby(by='Sex')['Amt'].max()

# Transpose dataframe
employee.transpose()
employee.T




