import pandas as pd
import numpy as np

'''
A panel is a 3D container of data.
A Panel can be created using the following constructor:
   pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
   - data: Data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame
   - items: axis=0, each item corresponds to a DataFrame contained inside.
   - major_axis: axis=1, it is the index (rows) of each of the DataFrames.
   - minor_axis: xis=2, it is the columns of each of the DataFrames.
   - dtype: Data type of each column
   - copy: Copy data. Default, false
'''

################### Create Pannel ###################
## Create an Empty Panel
p = pd.Panel()
print(p)

## From 3D ndarray
data = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)

## From dict of DataFrame Objects
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)

################# Selecting the Data from Panel ##################

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
print(data['Item1'])
print(data['Item2'])

p = pd.Panel(data)
## Using Items
print(p['Item1'])

## Using major_axis
print(p.major_xs(1))  # row 1 for each item

## Using minor_axis
print(p.minor_xs(1))  # col 1 for each item
