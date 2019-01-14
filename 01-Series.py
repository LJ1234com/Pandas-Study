import pandas as pd
import numpy as np
'''
Series is a one-dimensional labeled array capable of holding data of any type. 
The axis labels are collectively called index.
A pandas Series can be created using the following constructor:
     pandas.Series( data, index, dtype, copy)
     - data: data takes various forms like ndarray, list, constants
     - index: Index values must be unique and hashable, same length as data. Default np.arrange(n) if no index is passed.
     - dtype: dtype is for data type. If None, data type will be inferred
     - copy: Copy data. Default False 
'''
################### Create Series ###################

# Create an Empty Series
s = pd.Series()
print(s)

# Create a Series from ndarray
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)

s = pd.Series(data, index=[10, 11, 12, 13])
print(s)

# Create a Series from dict
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
s = pd.Series(data)  # Dict keys are used to construct index.
print(s)

data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data,index=['b','c','d','a']) # Index order is persisted and the missing element is filled with NaN
print(s)

# Create a Series from Scalar
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)


################### Accessing Series ###################

# Accessing Data from Series with Position
s = pd.Series([1, 2, 3, 4, 5], index=['a','b','c','d', 'e'])
print(s)
print(s[0])
print(s[[0, 2, 4]])
print(s[:3])
print(s[-3:])

# Accessing Data Using Label (Index)
print(s['a'])
print(s[['a', 'c', 'd']])
