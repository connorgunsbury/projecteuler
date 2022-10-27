# Find the sum of all the primes below two million.
import math
def isPrime(num):
    if num == 1:
        return False
    for i in range(2,math.floor(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True
sum = 0
n = 10
for i in range(0,n+1):
    if isPrime(i):
        sum += i

print(sum)