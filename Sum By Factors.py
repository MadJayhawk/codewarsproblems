'''
4 kyu  Python
https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python


'''

def primes(n):
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n//3)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)//3)      ::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
        sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
    a= [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]
    return a

def sum_for_list(z):
    n = abs(max(z, key=abs))
    e = {}
    p=primes(n+1)
    for j in z:
        h=j
        if j<0:
            h=-1*j
        for i in p:
            if h%i == 0:
                if i not in e:
                    e[i]=j
                else:
                    e[i]+=j
                h=h//i
                if h<=1:
                    break
    return sorted([[k,v] for k, v in e.items()])

if __name__ == "__main__":
    x = [961661, -127944, -906824, -796969, -105165, 459607, -95005, -599227, -586847, -825044] #[15, 21, 24, 30, 45]
    print(sum_for_list(x))
    print()
'''
def sum_for_list(lst):
    factors = {i for k in lst for i in xrange(2, abs(k)+1) if not k % i}

    prime_factors = {i for i in factors if not [j for j in factors-{i} if not i % j]}

    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]
    ------------------------------------------
    from collections import defaultdict


def prime(x):
    for i in xrange(2, x):
        if x % i == 0:
            return False
    return True


def prime_dividers(a):
    return (x for x in xrange(2, abs(a) + 1) if a % x == 0 and prime(x))


def sum_for_list(lst):
    d = defaultdict(int)
    for a in lst:
        for div in prime_dividers(a):
            d[div] += a
    return sorted([list(item) for item in d.iteritems()])

'''




