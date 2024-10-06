# 5 kyu  Python
# https://www.codewars.com/kata/588833be1418face580000d8/train/python
import pytest
import cProfile,pstats,io
from pstats import SortKey

import time
def three_split(seq):
    d=[]
    cnt=0
    pr=cProfile.Profile()
    pr.enable()
    for i in range(1, len(seq)+1):
        # tic = time.perf_counter()
        a = sum(seq[0:i])
        for j in range(i, len(seq)):
            if i != j:
                # print( sum(seq[0:i]),sum(seq[i:j]),sum(seq[j:len(seq)+1]))
                # print(seq[0:i], seq[i:j], seq[j:len(seq) + 1])
                # print(sum(seq[0:i])==sum(seq[i:j])==sum(seq[j:len(seq)+1]))

                b=sum(seq[i:j])
                if a==b:
                    c = sum(seq[j:len(seq) + 1])
                    if a==c:
                        cnt+=1
            # print()
        # toc = time.perf_counter()
        # print(f"Loops: {toc - tic:0.7f} seconds")
    pr.disable()
    s=io.StringIO()
    sortby=SortKey.CUMULATIVE
    ps=pstats.Stats(pr,stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
    return cnt


if __name__ == '__main__':
    a=[-1,1,-2,2,-3,3,-4,4]
    print(three_split(a))
---------------------------------------------------------------
'''
def three_split(seq):
    #quick, exhaustive approach took too long
    count = 0
    a=0
    b=0
    c=0
    
    #I need a little more efficiency. Let's see what I can do with "sum"
    #Yep "sum" was what really killed me the naivest initial approach was at least n^6. Now it's just n^2 and that works for me  
    tot_sum = sum(seq)
    for i in range(0, len(seq)-2):
        a += seq[i]  # keep a running sum for a, it's just the next value added in
        b = 0 
        for j in range(i+1, len(seq)-1):
            b += seq[j]  # b starts each of its loops equal to the number just one right of 'a'
            c = tot_sum - b - a  # c is whatever is left of the total when a and b are taken away. 
            if a == b and b == c:
                count += 1
    
    return count
'''
'''
def three_split(arr):
    s = sum(arr)
    a=0
    b=0
    c=0
    d=0
    for i in arr:
        c,d = b,d+i
        if d == 2*s/3:
            b += a
        if d == s/3:
            a += 1
    return c
if __name__ == '__main__':
    a=[-1,1,-2,2,-3,3,-4,4]
    print(three_split(a))
'''
    

