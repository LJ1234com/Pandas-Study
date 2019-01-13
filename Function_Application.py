import pandas as pd
import numpy as np
'''
 pipe():      Table wise Function Application
 apply():     Row or Column Wise Function Application
 applymap():  Element wise Function Application on DataFrame
 map():       Element wise Function Application on Series
'''


############### Table-wise Function Application ###############
def adder(ele1, ele2):
   return ele1 + ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df)
df2 = df.pipe(adder, 2)
print(df2)


############### Row or Column Wise Function Application ###############
print(df.apply(np.mean))  # By default, the operation performs column wise
print(df.mean())

print(df.apply(np.mean,axis=1))  # operations can be performed row wise
print(df.mean(1))

df2 = df.apply(lambda x: x - x.min())
print(df2)

############### Element wise Function Application ###############
df['col1'] = df['col1'].map(lambda x: x * 100)
print(df)

df = df.applymap(lambda x:x*100)
print(df)
