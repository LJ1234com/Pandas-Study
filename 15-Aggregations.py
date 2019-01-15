import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print(df)

r = df.rolling(window=2, min_periods=1)
print(r)

## Apply Aggregation on a Whole Dataframe
print(r.aggregate(np.sum))
## Apply Aggregation on a Single Column of a Dataframe
print(r['A'].aggregate(np.sum))

## Apply Aggregation on Multiple Columns of a DataFrame
print(r[['A', 'B']].aggregate(np.sum))

## Apply Multiple Functions on a Single Column of a DataFrame
print(r['A'].aggregate([np.sum, np.mean]))

## Apply Multiple Functions on Multiple Columns of a DataFrame
print(r[['A', 'B']].aggregate([np.sum, np.mean]))

## Apply Different Functions to Different Columns of a Dataframe
print(r.aggregate({'A': np.mean, 'B': np.sum}))
