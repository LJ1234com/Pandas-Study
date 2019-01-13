import pandas as pd
import numpy as np

'''
A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
A pandas DataFrame can be created using the following constructor:
     pandas.DataFrame( data, index, columns, dtype, copy)
     - data: data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame.
     - index: For the row labels, the Index to be used for the resulting frame is Optional Default np.arrange(n) if no index is passed.
     - columns: For column labels, the optional default syntax is - np.arrange(n). This is only true if no index is passed
     - dtype: Data type of each column.
     - copy: This command (or whatever it is) is used for copying of data, if the default is False.
'''

################### Create DataFrame ###################
## Create an Empty DataFrame
df = pd.DataFrame()
print(df)

## Create a DataFrame from Lists
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)

data = [[1, 2, 3, 4, 5]]
df = pd.DataFrame(data)
print(df)

data = [['Alex', 10], ['Bob', 12], ['Tom', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

data = [['Alex', 10], ['Bob', 12], ['Tom', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'], dtype=float)
print(df)

## Create a DataFrame from Dict of ndarrays / Lists
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28,34,29,42]}
df = pd.DataFrame(data)
print(df)

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

## Create a DataFrame from List of Dicts
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print(df)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print(df2)


## Create a DataFrame from Dict of Series
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)


################### Column Selection, Addition, and Deletion ###################
## Column Selection
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df['one'])

## Column Addition
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df['three']=pd.Series([10, 20, 30],index=['a','b','c'])
print(df)

df['four']=df['one'] + df['three']
print(df)

## Column Deletion -- del & pop
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([10, 20, 30], index=['a','b','c'])}
df = pd.DataFrame(d)
print(df)

del df['one'] # Columns can be deleted
print(df)

df.pop('two') # Columns can be popped
print(df)

################### Row Selection, Addition, and Deletion ###################
## Row Selection
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
print(df.loc['b'])  # SeSelection by Label
print(df.iloc[3])   # Selection by integer location
print(df[2:4])      # Slice Rows

## Row Addition
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
print(df)
print(df2)

df = df.append(df2)
print(df)

## Row Deletion
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
print(df)
print(df2)
df = df.append(df2)
print(df)
# Drop rows with label 0
df = df.drop(0)
print(df)
