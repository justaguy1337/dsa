def NnumbersSum(n):
    if n==0:
        return 0
    return n + NnumbersSum(n-1)

if __name__ == '__main__':
    N = 4
    print(NnumbersSum(N))