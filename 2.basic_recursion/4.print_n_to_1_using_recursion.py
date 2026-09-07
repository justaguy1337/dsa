def printNumbers(n):
    if n == 0:
        return
    print(n)
    printNumbers(n-1)

if __name__ == '__main__':
    N = 10
    printNumbers(N)