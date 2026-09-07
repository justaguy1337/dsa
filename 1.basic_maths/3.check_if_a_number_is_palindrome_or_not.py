def palindrome(n):
    dup = n
    ans = 0
    while dup > 0:
        temp = dup % 10
        ans = ans * 10 + temp
        dup //= 10
    return n == ans

if __name__== '__main__':
    N = 1221
    print(palindrome(N))