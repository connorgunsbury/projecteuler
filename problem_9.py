# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for i in range(1,1000):
    for j in range(1,1000):
        k = 1000 - i - j
        if i**2 + j**2 == k**2:
            # if i + j + k == 1000:
            print(i*j*k)