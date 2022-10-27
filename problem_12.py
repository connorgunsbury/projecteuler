# What is the value of the first triangle number to have over five hundred divisors?
# triangle numbers are the sum of the first n natural numbers
import math
def nat(i):
    return sum(range(1,i+1))

def numFactors(i):
    factors = 0
    for j in range(1,int(math.floor(math.sqrt(i)))+1):
        if i % j == 0: factors += 2
        if j*j == i: factors -= 1
    return factors

i = 2000
while True:
    if numFactors(nat(i)) > 500:
        print('500+ factor triangular number: ' + str(nat(i)))
        break
    i += 1