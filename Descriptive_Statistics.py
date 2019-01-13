import pandas as pd
import numpy as np
'''
 count()	Number of non-null observations
 sum()	    Sum of values for the requested axis. By default, axis is index (axis=0).
 mean()	    Mean of Values
 median()	Median of Values
 mode()	    Mode of values
 std()	    Standard Deviation of the Values
 min()	    Minimum Value
 max()	    Maximum Value
 abs()	    Absolute Value
 prod()	    Product of Values
 cumsum()	Cumulative Sum
 cumprod()	Cumulative Product
 describe() function computes a summary of statistics pertaining to the DataFrame columns.   

'''

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

df = pd.DataFrame(d)
print(df)

## axis can be specified
print(df.sum())  # axis=0
print(df.mean())
print(df.std())

# print(df.sum(1)) # axis=1
# print(df.mean(1))
# print(df.std(1))


print(df.count())
print(df.median())
print(df.min())
print(df.max())
print(df.prod())
print(df.cumsum())

## Summarizing Data
print(df.describe())                  # number: Summarizes Numeric columns. by default, 'number'.
print(df.describe(include='object'))  # object: Summarizes String columns
print(df. describe(include='all'))    # all:Summarizes all columns together (Should not pass it as a list value)
