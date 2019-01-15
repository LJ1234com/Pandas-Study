import pandas as pd
import numpy as np

'''
Pandas provides various facilities for easily combining together Series, DataFrame, and Panel objects.
    pd.concat(objs,axis=0,join='outer',join_axes=None, ignore_index=False)
 -objs:          This is a sequence or mapping of Series, DataFrame, or Panel objects.
 -axis:          {0, 1, ...}, default 0. This is the axis to concatenate along.
 -join:          {'inner', 'outer'}, default 'outer'. How to handle indexes on other axis(es). Outer for union and inner for intersection.
 -ignore_index:  boolean, default False. If True, do not use the index values on the concatenation axis. The resulting axis will be labeled 0, ..., n-1.
 -join_axes:     This is the list of Index objects. Specific indexes to use for the other (n-1) axes instead of performing inner/outer set logic.
'''
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print(one)
print(two)

print(pd.concat([one,two]))
print(pd.concat([one,two], keys=['x','y']))
print(pd.concat([one,two],keys=['x','y'],ignore_index=True))
print(pd.concat([one,two],axis=0))
print(pd.concat([one,two],axis=1))


## Concatenating Using append
print(one.append(two))
print(one.append([two,one,two]))

######################### Time Series #####################
## Get Current Time
print(pd.datetime.now())

## Create a TimeStamp
print(pd.Timestamp('2017-03-01'))
print(pd.Timestamp(1587687255,unit='s'))

## Create a Range of Time
print(pd.date_range("11:00", "13:30", freq="30min").time)

## Converting to Timestamps
print(pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None])))
print(pd.to_datetime(['2005/11/23', '2010.12.31', None]))
