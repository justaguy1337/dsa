def selectionSort(arr):
    n = len(arr)

    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print(arr)
    selectionSort(arr)
    print(arr)