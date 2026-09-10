def KtimesRotateArray(arr,k):
    N = len(arr)

    N = k % N

    x = arr[:N]
    y = arr[N:]
    return y+x

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    x = KtimesRotateArray(arr,k)

    print(x)