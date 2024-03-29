"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    >>> read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    >>> read_numbers(5)
    No numbers entered

"""


def read_numbers(*args):
    count=0
    sum=0
    avg=0
    for i in args:
        if(isinstance(i,int)):
            count+=1
            sum+=i
        if(count==0):
            print("No numbers entered") 
            return  
    avg=float(sum/count)    
    print(format(avg,".2f"))
read_numbers(1, 2, 'hello', 2, 'world')        





