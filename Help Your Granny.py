from math import sqrt

def dis(h,s):
    return sqrt((h**2)-(s**2))

def tour (a,b,c):
    d=[]
    for i,j in b:
        for k in a:
            if k==i:
                d.append(c[j])
    p=list(zip(d[0:],d[1:]))
    sm=d[0]+d[-1]
    for i,j in p:
        sm+=dis(j,i)
    return int(sm)

'''
def tour(friends, friend_towns, home_to_town_distances):
    res=0
    s=0
    for i in friend_towns:
        if i[0] in friends:
            res=res+(home_to_town_distances[i[1]]**2-s**2)**(0.5)
            s=home_to_town_distances[i[1]]
    res=res+s
    return int(res)
------------------------------------------------
import math

def tour(f, ft, h):
    l = sorted(v for k, v in h.iteritems() if k in (v_ for k_, v_ in ft if k_ in f))
    res = l[0]
    while len(l) > 1:
        a = l.pop(0)
        res += math.sqrt(l[0] ** 2 - a ** 2)
    return int(res + l[0])
'''