'''

5 kyu  Python
https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

'''


def prt(desc,*args):
    print() 
    print(desc,": ",*args) 


import math
from functools import reduce

def list_squared(a,b):
    prt('a-b',a,b)
    d=[] 
    for n in range(a,b):   
        r= sum([j**2 for j in set(reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))])
        a = math.sqrt(r)
        if int(a + 0.5) ** 2 == r:
            d.append([n,r])      
    return d
     
if __name__ == '__main__': 
    m,n = [42,250]
    prt(list_squared(m,n))
'''
rajat004

def divi(n):
    fac = set()
    for i in range(1, int(n**.5)+1):
        if n % i == 0:
            fac.add(i**2)
            fac.add(int(n/i)**2)
    return fac

def list_squared(m, n):
    return [[i, sum(divi(i))] for i in range(m, n) if str(sum(divi(i))**.5)[-1] == '0']
'''