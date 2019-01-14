import pandas as pd
import numpy as np

############### Iterating a Series ###############
s = pd.Series(np.array(['a', 'b', 'c', 'd']))
print(s)

for i in s:
    print(i)


############### Iterating a DataFrame ###############
'''
iteritems()   Iterates over each column as key, value pair with label as key and column value as a Series object.
iterrows()    returns the iterator yielding each index value along with a series containing the data in each row.
itertuples()  return an iterator yielding a named tuple for each row in the DataFrame.

'''


N=20
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })
print(df)

for col in df:
    print(col)

for key, value in df.iteritems():
    print(key, value)

for row_index, row in df.iterrows():
    print(row_index, row)

for row in df.itertuples():
    print(row)
