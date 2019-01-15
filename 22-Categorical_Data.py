import pandas as pd
import numpy as np

'''
 -category         By specifying the dtype as "category" in pandas object creation.
 -pd.Categorical   Using the standard pandas Categorical constructor, we can create a category object.
 -.describe()      command on the categorical data, we get similar output to a Series or DataFrame of the type string.

'''

s = pd.Series(["a","b","c","a"], dtype="category")
print(s)

cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print(cat)

cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print(cat)

cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print(cat)

## Description
cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"cat":cat, "s":["a", "c", "c", np.nan]})
print(df.describe())

print(df["cat"].describe())

## Get the Properties of the Category
s = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print(s.categories)

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print(cat.ordered) # The function returned false because we haven't specified any order.


## Renaming Categories
s = pd.Series(["a","b","c","a"], dtype="category")
print(s)
s.cat.categories = ["Group %s" % g for g in s.cat.categories]
print(s.cat.categories)

## Appending New Categories
s = pd.Series(["a","b","c","a"], dtype="category")
s = s.cat.add_categories([4])
print(s.cat.categories)

## Removing Categories
s = pd.Series(["a","b","c","a"], dtype="category")
print(s)
print(s.cat.remove_categories("a"))
