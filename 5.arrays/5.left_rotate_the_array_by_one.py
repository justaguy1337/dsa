def rotateArray(arr):
    temp = arr[0]

    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr[i] = temp

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    rotateArray(arr)
    print(arr)