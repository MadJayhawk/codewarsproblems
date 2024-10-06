# 5 kyu  Python
# https://www.codewars.com/kata/permutation-position/train/python
trans_table = str.maketrans('abcdefghijklmnopqrstuvwxyz',
              '0123456789abcdefghijklmnop')

def permutation_position(perm):
    return int(perm.translate(trans_table), 26) + 1

if __name__ == '__main__':
    print(permutation_position('foo'))