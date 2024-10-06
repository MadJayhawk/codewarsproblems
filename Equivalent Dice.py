''' 
5 kyu  Python
https://www.codewars.com/kata/5b26047b9e40b9f4ec00002b

started:  8/29/24
completed: 

'''

def factor_lists(n, min_factor=3, max_factor=20):
    result = set()
    
    def backtrack(current_product, current_list, start):
        if current_product == n and len(current_list) >= 2:
            result.add(tuple(sorted(current_list)))
            return
        
        for i in range(start, max_factor + 1):
            if current_product * i > n:
                break
            if n % i == 0 and min_factor <= i <= max_factor:
                backtrack(current_product * i, current_list + [i], i)
    
    backtrack(1, [], min_factor)
    return [list(x) for x in result if all(min_factor <= y <= max_factor for y in x)]

# Example usage
number = 36
factors = factor_lists(number)
cnt=0
for factor_list in sorted(factors):
    print(factor_list)
    cnt+=1
print(f'count: {cnt-1}')