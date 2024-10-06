# # https://www.geeksforgeeks.org/find-all-combinations-that-adds-upto-given-number-2/

n = 5
a = [1] * 5
t = 0
h = 4
d = []
c = []
while t!=0:


#
# for i in range(0, 6):
#
#     print(sum(a))
#
# print(a)

# for h in range(1, n + 1):
#     for i in range(h, n + 1):
#         for j in range(i, n + 1):
#
#             a[0] = h
#             a[1] = i
#             a[2] = j
#
#             print(a)

#
# # arr - array to store the combination
# # index - next location in array
# # num - given number
# # reducedNum - reduced number
# def findCombinationsUtil(arr, index, num, reducedNum, c):
#     # Base condition
#     if reducedNum < 0:
#         return
#
#     # # If combination is found, print it
#     print("aa", sum(arr[:index]), arr[:index], reducedNum, c)
#
#     if reducedNum == 0:
#
#         for i in range(index):
#             print(arr[i], end=" ")
#         print("")
#         return
#
#     # Find the previous number stored in arr[].
#     # It helps in maintaining increasing order
#     prev = 1 if (index == 0) else arr[index - 1]
#
#     # note loop starts from previous
#     # number i.e. at array location
#     # index - 1
#     for k in range(prev, num + 1):
#         # next element of array is k
#         arr[index] = k
#         c += 1
#         # call recursively with
#         # reduced number
#         findCombinationsUtil(arr, index + 1, num, reducedNum - k, c)
#
#     # Function to find out all
#
#
# # combinations of positive numbers
# # that add upto given number.
# # It uses findCombinationsUtil()
# def findCombinations(n, c):
#     # array to store the combinations
#     # It can contain max n elements
#     arr = [0] * n
#
#     # find all combinations
#     findCombinationsUtil(arr, 0, n, n, c)
#
#
# # Driver code
# n = 5
# findCombinations(n, 0)
