# sum the digits of the number 2^1000
base = 2
power = 1000
s = str(base**power)
sum = 0
for dig in s: sum += int(dig)
print(sum) 