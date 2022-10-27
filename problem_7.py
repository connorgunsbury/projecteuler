# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import math
def isPrime(num):
    for i in range(2,math.floor(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True
i = 2
pc = 0
while True:
    if isPrime(i):
        pc += 1
        if pc == 10001:
            print(i)
            break
    i += 1