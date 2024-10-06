'''

6 kyu  Python
https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

'''
def delete_nth(order,max_e):
   counter = {}
   d=[]
   for x in order:
      if x not in counter:
         counter[x] = 0
      counter[x] += 1
      if counter[x]<=max_e:
         d.append(x) 
   return d

if __name__ == "__main__":
    a = [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1] #[1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5]
    n=3
    print(delete_nth(a,n))
    print()