def insertion_sort(arr, i, n):
    if i == n:
        return

    j = i

    while j > 0 and arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j-=1

    insertion_sort(arr, i+1, n)

if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print(arr)
    insertion_sort(arr, 0, len(arr))
    print(arr)