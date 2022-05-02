# Permutations
from math import factorial

def fact(n):
    return factorial(n)
f = fact(6)

def permutations(n, r):
    nPr = fact(n) / fact(n-r)
    return nPr

x = permutations(5,4)
# print(x)

def combinations(n, r):
    nCr = fact(n) / fact(r) * fact(n-r)
    return nCr
y = combinations(6,3)
print(y)
