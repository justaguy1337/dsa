def bubble_sort(arr, n):
    if n == 1:
        return

    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

    bubble_sort(arr, n-1)

if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print(arr)
    bubble_sort(arr, len(arr))
    print(arr)