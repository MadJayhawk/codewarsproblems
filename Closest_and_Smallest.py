'''

5 kyu  Python
https://www.codewars.com/kata/5868b2de442e3fb2bb000119/train/python

'''
import itertools
def sum_digits(n): 
    s = 0 
    while n: 
        s += n % 10 
        n //= 10 
    return s

def closest(s):
    if s=="":
        return []
    d=[]
    cnt=0
    for i in (map(int,s.split())):
        d.append([sum_digits(i),cnt,i]) 
        cnt +=1
    b=list(itertools.combinations(d,2))
    d=[]
    for i in b:
        a=[abs(i[0][0]-i[1][0])]
        d.append([[abs(i[0][0]-i[1][0])],[i[0][0]+i[1][0]],[i[0][1]+i[1][1]],i]) 
    d.sort(key=lambda x:x[0]+x[1]+x[2])
    return sorted(d[0][3])

print(closest("456899 50 11992 176 272293 163 389128 96 290193 85 52"))

'''
def closest(s):
    wght = sorted([ [sum(int(c) for c in n), i, int(n)] for i, n in enumerate(s.split()) ], key=lambda k: (k[0], k[1]))
    diff = [ abs(a[0] - b[0]) for a, b in zip(wght, wght[1:]) ]
    return  [ wght [diff.index(min(diff)) ], wght [diff.index(min(diff)) + 1] ] if wght else []
    -----------------------------------------------
def closest(strng):
    if (strng == ""): return []
    nums, l, i = strng.split(), [], 0
    for n in nums:
        s = sum(list(int(i) for i in n))
        l += [[s, i, int(n)]]
        i += 1
    l.sort()
    valmin, argmin = min((l[i][0] - l[i - 1][0], i) for i in range(1, len(l)))
    return [l[argmin - 1], l[argmin]]
'''