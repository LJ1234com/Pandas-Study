import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(5, 2),index=[1,4,6,2,3],columns=['col2','col1'])
print(df)

################# By Label ####################
df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
print(df)

print(df.sort_index())
print(df.sort_index(ascending=False))
print(df.sort_index(axis=1))

################# By Value ####################
print(df.sort_values(by='col1'))
print(df.sort_values(by='col1', ascending=False))
print(df.sort_values(by='col1', kind='mergesort'))
