def removeDuplicates(arr):
    N = len(arr)
    i = 0
    for j in range(1,N):
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
    return i+1

if __name__ == "__main__":
    arr = [1,1,2,2,2,3,3] 
    x = removeDuplicates(arr)
    print(arr[:x])