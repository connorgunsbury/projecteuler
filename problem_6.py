# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
ss = 0
for i in range(1,101):
    ss += i**2

s = sum(range(1,101))**2

print(s - ss)