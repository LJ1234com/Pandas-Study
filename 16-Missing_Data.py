import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'],
                                        columns=['one', 'two', 'three'])

print(df)

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)

## Check for Missing Values
print(df.isnull())
print(df.notnull())

print(df['one'].isnull())
print(df['one'].notnull())

## Calculations with Missing Data
print(df['one'].sum()) # NA will be treated as Zero, If the data are all NA, then the result will be NA

## Cleaning / Filling Missing Data
'''
Pandas provides various methods for cleaning the missing values. 
The fillna function can 'fill in' NA values with non-null data in a couple of ways, 
which we have illustrated in the following sections.
'''

## Replace NaN with a Scalar Value
print(df.fillna(0))

## Fill NA Forward and Backward
'''
 pad/fill	    Fill methods Forward
 bfill/backfill	Fill methods Backward
'''
print(df.fillna(method='pad'))
print(df.fillna(method='bfill'))

## Drop Missing Values
'''
If you want to simply exclude the missing values, then use the dropna function along with the axis argument. 
By default, axis=0, i.e., along row, which means that if any value within a row is NA then the whole row is excluded.
'''
print(df.dropna())
print(df.dropna(axis=1))


## Replace Missing (or) Generic Values
'''
Many times, we have to replace a generic value with some specific value. 
We can achieve this by applying the replace method.
Replacing NA with a scalar value is equivalent behavior of the fillna() function.
'''
df = pd.DataFrame({'one':[10,20,30,40,50,2000],
                   'two':[1000,0,30,40,50,60]
                   }
                  )
print(df)
print(df.replace({1000: 10, 2000: 60}))
