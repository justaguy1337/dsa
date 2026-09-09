def secondLargest(arr, n):
    if n < 2:
        return -1
    
    first, second = float('-inf'), float('-inf')

    for i in arr:
        if i > first:
            second = first
            first = i
        elif first > i > second:
            second = i

    return second

def secondSmallest(arr, n):
    if n < 2:
        return -1
    
    first, second = float('inf'), float('inf')

    for i in arr:
        if i < first:
            second = first
            first = i
        elif first < i < second:
            second = i

    return second


if __name__ == "__main__":
    arr = [8, 10, 5, 7, 9] 
    N = len(arr)
    print("Second Largest: ",secondLargest(arr, N))
    print("Second Smallest: ",secondSmallest(arr, N))