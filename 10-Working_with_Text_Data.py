import pandas as pd       
import numpy as np        
                          
'''                       
 lower()	            Co
 upper()	            Co
 len()	                Co
 strip()	            He
 split(' ')	            Sp
 cat(sep=' ')	        Co
 get_dummies()	        Re
 contains(pattern)	    Re
 replace(a,b)	        Re
 repeat(value)	        Re
 count(pattern)	        Re
 startswith(pattern)	Re
 endswith(pattern)	    Re
 find(pattern)	        Re
 findall(pattern)	    Re
 swapcase	            Sw
 islower()	            Ch
 isupper()             	Ch
 isnumeric()	        Ch
'''                       
                          
s = pd.Series(['Tom', 'Wil
print(s)                  
print(s.str.lower())      
print(s.str.upper())      
print(s.str.len())        
print(s.str.strip())      
print(s.str.split(' '))   
print(s.str.cat(sep='_')) 
print(s.str.get_dummies())
print(s.str.contains(' '))
print(s.str.replace('@', '
print(s.str.repeat(2))    
print(s.str.count('m'))   
print(s.str.startswith('T'
print(s.str.endswith('t'))
print(s.str.find('e'))    
print(s.str.findall('e')) 
print(s.str.swapcase())   
print(s.str.islower())    
print(s.str.isupper())    
print(s.str.isnumeric())  
