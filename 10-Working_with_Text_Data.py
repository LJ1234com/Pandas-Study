import pandas as pd
import numpy as np

'''
 lower()	            Converts strings in the Series/Index to lower case.
 upper()	            Converts strings in the Series/Index to upper case.
 len()	                Computes String length().
 strip()	            Helps strip whitespace(including newline) from each string in the Series/index from both the sides.
 split(' ')	            Splits each string with the given pattern.
 cat(sep=' ')	        Concatenates the series/index elements with given separator.
 get_dummies()	        Returns the DataFrame with One-Hot Encoded values.
 contains(pattern)	    Returns a Boolean value True for each element if the substring contains in the element, else False.
 replace(a,b)	        Replaces the value a with the value b.
 repeat(value)	        Repeats each element with specified number of times.
 count(pattern)	        Returns count of appearance of pattern in each element.
 startswith(pattern)	Returns true if the element in the Series/Index starts with the pattern.
 endswith(pattern)	    Returns true if the element in the Series/Index ends with the pattern.
 find(pattern)	        Returns the first position of the first occurrence of the pattern.
 findall(pattern)	    Returns a list of all occurrence of the pattern.
 swapcase	            Swaps the case lower/upper.
 islower()	            Checks whether all characters in each string in the Series/Index in lower case or not. Returns Boolean
 isupper()             	Checks whether all characters in each string in the Series/Index in upper case or not. Returns Boolean.
 isnumeric()	        Checks whether all characters in each string in the Series/Index are numeric. Returns Boolean.
'''

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
print(s)
print(s.str.lower())
print(s.str.upper())
print(s.str.len())
print(s.str.strip())
print(s.str.split(' '))
print(s.str.cat(sep='_'))
print(s.str.get_dummies())
print(s.str.contains(' '))
print(s.str.replace('@', '$'))
print(s.str.repeat(2))
print(s.str.count('m'))
print(s.str.startswith('T'))
print(s.str.endswith('t'))
print(s.str.find('e'))
print(s.str.findall('e'))
print(s.str.swapcase())
print(s.str.islower())
print(s.str.isupper())
print(s.str.isnumeric())
