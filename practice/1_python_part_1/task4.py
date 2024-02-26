"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List


def calculate_power_with_difference(list1):
    new_list=[1]*3
    for i in range(len(list1)):
        if(i==0):
            new_list[i]=list1[i]**2
        else:
            new_list[i]=list1[i]**2-((list1[i-1]**2)-list1[i-1])
    print(new_list)  

calculate_power_with_difference([1, 2, 3])
    