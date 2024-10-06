''' 
6 kyu  Python
https://www.codewars.com/kata/59e19a747905df23cb000024/train/python

completed: 1-27-2024

'''

def find(s):
    for c in range(1,2000):
        for i in range(0, len(s)-c, c):
            x=[int(s[i:i+c])+1 for i in range(0, len(s)-c, c)]
            print(s,c,x,len(s),int(s[i:i+c]))


            # if s[0:c]+''.join(str(num) for num in x)==s:
            #       return s
            # else:
            #       return s[:c]


print(find("17181920"))