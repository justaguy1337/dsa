def check(arr):
    for i in range(len(arr)-1):
        if not arr[i] <= arr[i+1]:
            return False
    return True

if __name__ == "__main__":
    arr = [1,2,3,4,5] 
    print(check(arr))