"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math
class OperationNotFoundException(Exception):
    pass

def math_calculate(function,*args):
    if function=='sqrt':
        if len(*args)==1:
            print(math.sqrt(args[0]))
        else:
            raise OperationNotFoundException("Argument does not match with the math function")  
    if function=='pow':
        print(len(args))
        if len(args)==2:
            print(math.pow(*args))
        else:
            raise OperationNotFoundException("Argument does not match with the math function") 
    if function=='log10':
        if len(*args)==1:
            print(math.log10(args[0]))
        else:
            raise OperationNotFoundException("Argument does not match with the math function")
    if function=='ceil':
        if len(*args)==1:
            print(math.ceil(args[0]))
        else:
            raise OperationNotFoundException("Argument does not match with the math function")               
math_calculate('pow', 2,2)     