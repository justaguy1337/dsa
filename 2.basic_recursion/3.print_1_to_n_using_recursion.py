def printNumbers(n):
    if n == 0:
        return
    printNumbers(n-1)
    print(n)

if __name__ == '__main__':
    N = 10
    printNumbers(N)