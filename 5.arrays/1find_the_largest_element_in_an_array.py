def largest(arr):
    res = 0
    for i in arr:
        if res <= i:
            res = i
    return res

if __name__ == "__main__":
    arr = [8, 10, 5, 7, 9] 
    print(largest(arr))