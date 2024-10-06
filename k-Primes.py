# 5 kyu  Python
# https://www.codewars.com/kata/xxxxxx/python

# def count_Kprimes(k, start, end):
#     # your code
#
# def puzzle(s):
#     # your code
import math


k = 5
start = 2
end = 100
d = []
for num in range(start, 500):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        d.append(num)
print("d: ", d)
print("---------------------------")
f = d.copy()
print("f: ", f)

r = []
for i in range(0, len(d) + 1):
    for j in range(i, len(f)):
        k = d[i] * f[j]
        if k <= end + 1:
            r.append(k)

print("r: ", set(sorted(r)))
print("----------------------------")
e = []
for i in range(0, len(d) + 1):
    for j in range(i, len(r)):
        k = d[i] * r[j]
        if k <= end + 1:

            e.append(k)

print("e: ", set(sorted(e)))
print(
    "--------------------------------------------------------------------------------------------"
)

#
# e = [[4, 5, 6, 7, 8]]
# for i in range(1, k):
#     g = []
#     for j in e:
#         for r in f:
#             if r * j < end:
#                 g.append(r * j)
#
#     g.sort()
#     h = list(set(g))
#     hh = []
#     for c in h:
#         if c >= 1000 and c <= 1100:
#             hh.append(c)
#     f = h.copy()
#     print("h:", sorted(hh))

# [4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87,
#  91, 93, 94, 95])
# {4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95}
