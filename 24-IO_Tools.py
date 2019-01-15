import pandas as pd
import numpy as np

'''
pandas.read_csv(filepath_or_buffer, 
                sep=',', 
                delimiter=None, 
                header='infer',
                names=None, 
                index_col=None, 
                usecols=None
               )
'''

df=pd.read_csv("tmp.csv")
print(df)

## custom index
df=pd.read_csv("tmp.csv",index_col=['Name'])
print(df)

## Converters
df = pd.read_csv("tmp.csv", dtype={'Salary': np.float64})
print(df)
print(df.dtypes)

## header_names
df=pd.read_csv("tmp.csv", names=['a', 'b', 'c','d','e'])
print(df)

df=pd.read_csv("tmp.csv",names=['a','b','c','d','e'],header=0)
print(df)


## skiprows
df=pd.read_csv("tmp.csv", skiprows=2)
print(df)
