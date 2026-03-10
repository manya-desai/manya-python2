""" 1. Positive Indexing 
from array import array
arr = array('i',[10,20,30,40,50])
print(arr[0]) # first element
print(arr[2]) # third element
print(arr[4]) # fifth element """

""" 2. Negative Indexing
from array import array
arr = array('i',[10,20,30,40,50])
print(arr[-1]) # first element
print(arr[-2]) # third element
print(arr[-5]) # fifth element """

""" 3. Modifying elementsusing index 
from array import array
arr = array('i',[10,20,30,40,50])
arr[2] = 35
print(arr) """

""" 4. Index error """
from array import array
arr = array('i',[10,20,30])
print(arr[5]) 
