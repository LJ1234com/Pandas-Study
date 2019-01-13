import pandas as pd
import numpy as np


################## Series Basic Functionality ####################
'''
 - axes	    Returns a list of the row axis labels.
 - dtype	Returns the dtype of the object.
 - empty	Returns True if series is empty.
 - ndim	    Returns the number of dimensions of the underlying data, by definition 1.
 - size	    Returns the number of elements in the underlying data.
 - values	Returns the Series as ndarray.
 - head()	Returns the first n rows.
 - tail()	Returns the last n rows
'''

s = pd.Series(np.random.randn(4))  # numpy.random.randn(d0,d1,…,dn) return specific dim array, subject to gaussian distribution
print(s)
print(s.axes)
print(s.dtype)
print(s.empty)
print(s.ndim)
print(s.size)
print(s.values)
print(s.head(2))
print(s.tail(2))


################## DataFrame Basic Functionality ####################
'''
 - T	    Transposes rows and columns.
 - axes	    Returns a list with the row axis labels and column axis labels as the only members.
 - dtypes	Returns the dtypes in this object.
 - empty	True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.
 - ndim   	Number of axes / array dimensions.
 - shape	Returns a tuple representing the dimensionality of the DataFrame.
 - size	    Number of elements in the NDFrame.
 - values	Numpy representation of NDFrame.
 - head()	Returns the first n rows.
 - tail()	Returns last n rows.
'''
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

df = pd.DataFrame(d)
print(df)
print(df.T)
print(df.axes)
print(df.dtypes)
print(df.empty)
print(df.ndim)
print(df.shape)
print(df.size)
print(df.values)
print(df.head(2))
print(df.tail(2))
