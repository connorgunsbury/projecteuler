# grid problem
import math as m
def binom(n,k):
    return m.factorial(n)/(m.factorial(k)*m.factorial(n-k))

print(binom(40,20))