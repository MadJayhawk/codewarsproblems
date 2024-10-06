# 6 kyu  Python
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
def product_digits(n):
    s = 1
    while n:
        if n%10!=0:
            s*=( n % 10)
        n //= 10
    return s
   
def persistence(b):
    cnt=0
    t=b
    if '0' in str(b):
        return 1
    elif len(str(t))==1:
        return 0
    else:
        while len(str(t))!=1:
            cnt+=1
            if '0' in str(t):
                return cnt
            t=product_digits(t)
    return cnt
