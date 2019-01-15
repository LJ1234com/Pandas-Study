import pandas as pd

'''
 -String:    By passing a string literal, we can create a timedelta object.
 -Integer:   By passing an integer value with the unit, an argument creates a Timedelta object.
'''

print(pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))
print(pd.Timedelta(6,unit='h'))
print(pd.Timedelta(days=2))

################## Operations ##################

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
print(df)

## Addition
df['C']=df['A'] + df['B']
print(df)

## Subtraction
df['D']=df['C']-df['B']
print(df)
