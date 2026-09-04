
def getDivisors(n):
    ans = []

    for i in range(1,(n//2)+1):
        if n % i == 0:
            ans.append(i)
            # if n // i != i:
            #         ans.append(n // i)
    ans.append(n)
    return ans

if __name__== '__main__':
    N = 1000000
    print(getDivisors(N))