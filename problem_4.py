# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

pals = []
for i in range(0,999):
    for j in range(0,999):
        p = (999-i) * (999 - j)
        if str(p) == str(p)[::-1]:
            pals.append(p)

print(max(pals))