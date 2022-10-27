# find the number under 1 million with the longest collatz chain length to get to 1

# this function returns the next number in the sequence
def collatz(num, iter, orig):
    if num == 1:
        return iter
    if num % 2 == 0:
        iter += 1
        return collatz(num/2, iter, orig)
    else:
        return collatz(3*num+1, iter, orig)

startnum = 0
maxchainlength = 0
for i in range(1,1000001):
    chainlength = collatz(i,0,i)
    if chainlength > maxchainlength:
        maxchainlength = chainlength
        startnum = i

print(startnum)
