import math
def countDigits(n):
    return int(math.log10(n)) + 1

if __name__== '__main__':
    N = 329823
    print(countDigits(N))