import pandas as pd
import numpy as np

left = pd.DataFrame({
         'id': [1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id': ['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id': [1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id': ['sub2','sub4','sub3','sub6','sub5']})
print(left)
print(right)

## Merge Two DataFrames on a Key
print(pd.merge(left,right,on='id'))

## Merge Two DataFrames on Multiple Keys
print(pd.merge(left,right,on=['id','subject_id']))

################ Merge Using 'how' Argument ################
'''
left	LEFT OUTER JOIN	    Use keys from left object
right	RIGHT OUTER JOIN	Use keys from right object
outer	FULL OUTER JOIN	    Use union of keys
inner	INNER JOIN	        Use intersection of keys

'''

## Left Join
print(pd.merge(left, right, on='subject_id', how='left'))

## Right Join
print(pd.merge(left, right, on='subject_id', how='right'))

## Outer Join
print(pd.merge(left, right, on='subject_id', how='outer'))

## Inner Join
print(pd.merge(left, right, on='subject_id', how='inner'))
