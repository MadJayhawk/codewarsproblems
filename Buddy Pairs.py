'''

5 kyu  Python
https://www.codewars.com/kata/59ccf051dcc4050f7800008f/train/python

'''
from functools import reduce

def prt(desc,*args):
    print() 
    print(desc,": ",*args) 

def buddy(start, limit):
    a=set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))  # if not n % i instead of if n % i == 0

    return q
    
if __name__ == '__main__':
    x,y = 10, 50
    print(buddy(x,y))