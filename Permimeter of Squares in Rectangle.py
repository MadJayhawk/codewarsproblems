''' 
5 kyu  Python
https://www.codewars.com/kata/559a28007caad2ac4e000083/train/python

started: 7/25/24
completed: 8/29/24  Perplexity helped refine answer for large numbers

'''
def matrix_multiply(a, b, mod=None):
    c = [
        [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
        [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
    ]
    if mod:
        c = [[x % mod for x in row] for row in c]
    return c

def matrix_power(matrix, n, mod=None):
    result = [[1, 0], [0, 1]]  # Identity matrix
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, matrix, mod)
        matrix = matrix_multiply(matrix, matrix, mod)
        n //= 2
    return result

def fibonacci(n, mod=None):
    if n <= 1:
        return n
    matrix = [[1, 1], [1, 0]]
    result = matrix_power(matrix, n - 1, mod)
    return result[0][0]

def sum_fibonacci(n, mod=None):
    if n <= 0:
        return 0
    matrix = [[1, 1], [1, 0]]
    result = matrix_power(matrix, n + 2, mod)
    return result[0][0] - 1

def perimeter(n):
    return 4 * sum_fibonacci(n)


'''
def fib(n):
    a, b = 0, 1

    for i in range(n+1):
        if i == 0:
            yield b 
        else:
            a, b = b, a+b
            yield b
        

def perimeter(n):
    return sum(fib(n)) * 4


    --------------------------------

def perimeter(n):
    a, b = 1, 2
    while n:
        a, b, n = b, a + b, n - 1
    return 4 * (b - 1)

    
'''