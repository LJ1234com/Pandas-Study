import pandas as pd
import numpy as np

'''
 .loc() 	Label based
 .iloc()	Integer based
 .ix()          Both Label and Integer based
'''
## .loc()
df = pd.DataFrame(np.random.randn(8, 4), index=['a','b','c','d','e','f','g','h'], columns=['A', 'B', 'C', 'D'])
print(df)
print(df.loc[:, 'A'])         # select all rows for a specific column, <=> df['A']
print(df.loc[:, ['A', 'C']])  # Select all rows for multiple columns, say list[]
print(df.loc[['a','b','f','h'], ['A', 'C']]) # Select few rows for multiple columns, say list[]
print(df.loc['a':'h'])        # Select range of rows for all columns
print(df.loc['a'] > 0)    # for getting values with a boolean array

## .iloc()
print(df.iloc[:4])
print(df.iloc[1:5, 2:4])
print(df.iloc[[1, 3, 5], [1, 3]])
print(df.iloc[1:3, :])
print(df.iloc[:, 1:3])

## .ix()
print(df.ix[:4])
print(df.ix[:, 'A'])


## Attribute Access
print(df.A)
