# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:09:51 2019

@author: Mohit
"""

# A Employee dataframe with following data
import numpy as np
import pandas as pd
Employee = pd.DataFrame({'NAME':['ANITA','VIJAY','RAKESH','MAHESH','DINESH','SOURAV'],
                         'AGE':[36,37,49,20,38,44],
                         'SEX':['F','M','M','M','M','M'],
                         'SALARY':[23000,34000,25000,500000,300000,700000],
                         'GRADE':['A','A','B','A','B','B']})

#1. Show the top three and last three records.
Employee.head(3) #Top Three
Employee.tail(3) # Last Three
#2. Who has maximum salary among the 6 employees
Employee['SALARY'].max()
#3. Add another column “Department” to the data frame and assign value as Marketing for all the rows in that column
Employee['Department']=['Marketing']*6
Employee
#4. Group the data according to the GRADE column.
Employee.groupby(by='GRADE')
Employee

