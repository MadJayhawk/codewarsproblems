'''
5 kyu  Python
https://www.codewars.com/kata/54f8693ea58bce689100065f/train/python

'''
from fractions import Fraction
import math

def prt(desc,*args):
    print()
    print(desc,": ",*args) 

def decompose(a): 
    d=[]
    nom=0
    if a=='0': 
        return []  
    else:
        s=Fraction(a)
        if '.' in a:
            a=str(s)
        while True: 
            nom,den = list(map(int, a.split('/')))
            g=math.gcd(nom,den)
            if g!=1:
                nom//=g
                den//=g
            if nom%den==0:
                return [str(nom//den)]
            if nom==1:
                d.append(str(Fraction(1,den)))
                return d
            prt('nom-den',nom,den)
            y=den//nom+1
            prt('y',y)
            s-=Fraction(1,y) 
            d.append(str(Fraction(1,y)))
            prt('d',d)
            prt('s',s)
            a=str(s)
            prt('a',a)
        return a
c=decompose('2/8')
prt('answer',c)
'''
from math import ceil
from fractions import Fraction as F
def decompose(n):
    f = F(n)
    ff = int(f)
    result = [str(ff)] if ff else []
    f -= ff
    while f>0:
        x = F(1,int(ceil(f**-1)))
        f -= x
        result.append(str(x))
    return result
'''