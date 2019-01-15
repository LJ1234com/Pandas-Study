import pandas as pd
import numpy as np

'''
 .rolling() 
 .expanding()
 .ewm()
'''

df = pd.DataFrame(np.random.randn(10, 4),
index = pd.date_range('1/1/2000', periods=10),
columns = ['A', 'B', 'C', 'D'])

## rolling()
print(df)
print(df.rolling(window=2).mean())
print(df.rolling(window=2).sum())


## expanding()
print(df.expanding(min_periods=2).mean())
print(df.expanding(min_periods=2).sum())

## ewm()
print(df.ewm(com=0.5).mean())
