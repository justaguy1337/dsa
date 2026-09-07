def printName(i, n):
    if i > n:
        return
    
    print(f"{i}.dsa")
    printName(i + 1, n)

    i -= 1


if __name__ == '__main__':
    N = 10
    printName(1, N)
