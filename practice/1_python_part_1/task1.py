"""
Write function which deletes defined element from list.
Restriction: Use .pop method of list to remove item.
Examples:
    >>> delete_from_list([1, 2, 3, 4, 3], 3)
    [1, 2, 4]
    >>> delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
    ['a', 'c', 'd']
    >>> delete_from_list([1, 2, 3], 'b')
    [1, 2, 3]
    >>> delete_from_list([], 'b')
    []
"""
from typing import List, Any


def delete_from_list(list1,element):
    i=0
    while i<len(list1):
        if(list1[i]==element):
            list1.pop(i)
            i=i-1
        else:
            i=i+1
    print(list1)        
delete_from_list([1, 2, 3, 4, 3],3)    