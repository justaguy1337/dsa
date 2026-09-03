def reverse_a_number(n):
    ans = 0
    while n>0:
        temp = n%10
        ans = ans * 10 + temp
        n//= 10
    return ans

if __name__== '__main__':
    N = 12345
    print(reverse_a_number(N))