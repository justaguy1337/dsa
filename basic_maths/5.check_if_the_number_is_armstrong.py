import math

def ArmstrongChecker(n):
    k = int(math.log10(n))+1
    temp = n
    res = 0
    while temp > 0:
        dig = temp % 10
        res += dig ** k
        temp //= 10
    return res == n

if __name__== '__main__':
    N = 1634
    print(ArmstrongChecker(N))