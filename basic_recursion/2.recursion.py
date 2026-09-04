def printName(i,n):
    if i == n:
        return
    print(f"{i+1}.dsa")
    printName(i+1,n)


if __name__== '__main__':
    N = 10
    printName(0,N)