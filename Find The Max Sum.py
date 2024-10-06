"""
6 kyu
Simple Fun #302: Find The Max Sum
https://www.codewars.com/kata/59252121fb1f93fc8200013a

+----+----+----+
| a1 | a2 | a3 |
+----+----+----+
As shown above. There are three grids. Each grid fill in a number(let's call a1, a2 and a3). Such that 0 ≤ a1, a2, a3 ≤ n, where n is given, and meet the following rules:

- a1 + a2 is a multiple of 2;
- a2 + a3 is a multiple of 3;
- a1 + a2 + a3 is a multiple of 5;
Your task is to find a set of a1, a2, a3, which makes a1 + a2 + a3 maximum. Returns the sum of a1, a2, a3.

Started:  4/10/2023

Answer:

Completed:
"""


# Track the maximum value of t
def find_max_sum(n):
    if (n * 3) % 5 == 0 and (n * 2) % 3 == 0:
        answer = 3 * n
    else:
        if (2 * n) % 3 == 0:
            answer = 3 * n - (3 * n) % 5
        else:
            answer = 2 * n
    return answer

for i in range(3,31):
    print(find_max_sum(i))

# def find_max_sum(n):
#     max_sum=0
#     # for a1, a2, a3 in it.product(range(n + 1), range(n + 1), range(n + 1)):
#     for a1 in range(0,n+1):
#         for a2 in range(0,n+1):
#             for a3 in range(0,n+1):
#                 t=a1 + a2 + a3
#                 if t%5==0:
#                     if (a2 + a3) % 3 == 0:
#                         if (a1 + a2) % 2 == 0:
#                             max_sum = max(max_sum,t)
#     return max_sum

# for i in range(0,100):
#     print(f'{find_max_sum(i)} ')

# import itertools as it
# def find_max_sum(n):
#     max_sum=0
#     for a1, a2, a3 in it.product(range(n + 1), range(n + 1), range(n + 1)):

#         t=a1 + a2 + a3
#         print(t,t%5,a1,a2,a3)
#         if t%5==0:
#             max_sum = max(max_sum,t)
#     return max_sum
# for i in range(5,6):
#     print(f'{i}, {find_max_sum(i)} ')
# n=3
# x=[0,1,2,3,4,5]
# import itertools as it
# for i in it.product(x,x,x):
#     print(i,sum(i),sum(i)%5,(i[1]+i[0])%2,(i[1]+i[2])%3)
#     if sum(i)%5==0 and (i[1]+i[0])%2==0 and (i[1]+i[2])%3==0:
#         print('***',i,sum(i))
