"""
Write a function which divides x by y.
If y == 0 it should print "Division by 0" and return None
elif y == 1 it should raise custom Exception with "Deletion on 1 get the same result" text
else it should return the result of division
In all cases it should print "Division finished"
    >>> division(1, 0)
    Division by 0
    Division finished
    >>> division(1, 1)
    Division finished
    DivisionByOneException("Deletion on 1 get the same result")
    >>> division(2, 2)
    1
    Division finished
"""
import typing


class MyException(Exception):
    print("Deletion on 1 get the same result")

def division(x,y):
    if(y==0):
        print("Division by 0")
        print("Division finished")
        return None
    elif(y==1):
        print("Division finished")
        raise MyException()
    else:
        print(x/y)
        print("Division finished")
division(9,1)  
