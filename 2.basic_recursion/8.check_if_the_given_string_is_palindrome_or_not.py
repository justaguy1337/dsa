def palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return palindrome(s, left+1, right-1)


if __name__ == '__main__':
    s = "madam"
    N = len(s)
    print(palindrome(s, 0, N-1))