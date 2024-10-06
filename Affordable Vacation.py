''' 
5 kyu  Python
https://www.codewars.com/kata/66871953e441f6da6e36a0cc

started: 7/6/24
completed:   DID NOT COMPLETE

'''
def ratios(m,t):
    for i in t:
        r= [m//i for i in t if m//i>1 ]
    print(all(r))
    
    return r

def find_min_cost(money, days, cost):
    c=ratios(money,cost)
    return c

if __name__ == "__main__":
    x,y,z=100, 4, [1, 2, 3, 4, 555, 6, 7, 8, 9, 10]
    print(find_min_cost(x,y,z))

'''
10, 1, [5],
10, 1, [3, 2, 4]
10, 2, [3, 7, 6]
10, 1, [20, 15, 30]
10, 2, [9, 6, 7]
(50, 3, [10, 40, 5]
100, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
100, 5, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            '''