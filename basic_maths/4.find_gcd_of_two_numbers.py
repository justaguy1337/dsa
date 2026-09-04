def find_gcd(n1, n2):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1

    return n1 if n2 == 0 else n2

if __name__== '__main__':
    N1 = 13
    N2 = 129
    print(find_gcd(N1, N2))