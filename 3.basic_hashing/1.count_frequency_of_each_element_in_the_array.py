def frequency(arr):
    hash = {}

    for i in arr:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    return hash
if __name__ == '__main__':
    arr = [10,5,10,15,10,5]
    N = len(arr)
    ans = frequency(arr)

    for k, v in ans.items():
        print(f"{k} --> {v}")