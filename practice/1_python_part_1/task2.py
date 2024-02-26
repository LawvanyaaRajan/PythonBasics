"""
Write function which updates dictionary with defined values but only if new value more then in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)  # only b updated because new value for a less then original value
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {a: 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""
from typing import Dict


def set_to_dict(dict1,**keyword):
    for i in keyword:
        if i in dict1.keys():
            new_value=keyword[i]
            old_value=dict1[i]
            if(new_value>old_value):
                dict1[i]=keyword[i]
        else:
            dict1[i]=keyword[i]
    print(dict1) 
set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)  
