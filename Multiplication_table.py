# 6 kyu  Python
# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python


def multiplication_table(size):
   d=[]
   for i in range(1,size+1):
      d.append(i)
   g=[]
   g.append(d)
   k=1
   f=[]
   while k<=size-1:
      for i in d:
         f.append(i*d[k])
      g.append(f) 
      f=[]
      k+=1
   return g



if __name__ == "__main__":
    x = 10
    print(multiplication_table(5))
'''
def multiplicationTable(size):
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]

    
    -------------------------------
    def multiplication_table(size):
    n=1
    list1=[]
    list2=[]
    while n!=size+1:
        for i in range(1,size+1):
                list1.append(n*i)
        list2.append(list1)
        list1=[]
        n+=1
    return list2
               
   ----------------------------
   def multiplication_table(n):
    return [list(range(m, m * n + 1, m)) for m in range(1, n + 1)]
    
    '''