import pandas as pd
import numpy as np

N = 20
df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})

print(df)

df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
print(df_reindexed)

## Reindex to Align with Other Objects
df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
print(df1)
print(df2)

df1 = df1.reindex_like(df2)
print(df1)

## Filling while ReIndexing
'''
  pad/ffill        Fill values forward
  bfill/backfill   Fill values backward
  nearest          Fill from the nearest index values
'''

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
print(df1)
print(df2)

print(df2.reindex_like(df1))
print(df2.reindex_like(df1, method='ffill'))
print(df2.reindex_like(df1, method='backfill'))
print(df2.reindex_like(df1, method='nearest'))

## Limits on Filling while Reindexing
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
print(df1)
print(df2)
print(df2.reindex_like(df1))
print(df2.reindex_like(df1, method='ffill'))
print(df2.reindex_like(df1, method='ffill', limit=1)) # just fill one row

## Renaming
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df1)
print(df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
                 index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}))
