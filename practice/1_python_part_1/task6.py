"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple

 
def readFile(filename):
    tuple1=()
    list1=[]
    with open(r'C:\Users\lrajan\Desktop\project\PythonBasics\practice\1_python_part_1\filename.txt') as opened_file:
        for line in opened_file:
            list1.append(int(line))
        minn=min(list1)
        maxx=max(list1)
        tuple1=(minn,maxx)        
        print(tuple1)    
readFile('filename')    
