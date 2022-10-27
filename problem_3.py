#What is the largest prime factor of the number 600851475143?
import math
big = 600851475143

def isPrime(num):
    for i in range(2,math.floor(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

#def refactor(factor, big, biggestprime):
    
i = 2    
while True:
    if big % i == 0:    # this means that it is a factor
        if isPrime(i):  # this means that it is prime
            p = i       # save is as biggesst factor
            print(p)
        big = big / i
    i += 1
    if i > big:
        break
"""
p = 1
for num in range(1,big):
    if big % num == 0:
        if isPrime(num):
            p = num
"""
print(p)