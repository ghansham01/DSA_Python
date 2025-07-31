# Traditional Binary Search - Looking up if number is in array:
# Time Complexty: O(log n)
# Space Complexty: O(1)

def Search(arr, target):
    n = len(arr)
    L =0 
    R = n-1

    while L <= R:
        M = L + ((R-L) // 2)

        if arr[M] == target:
            return True
        elif target < arr[M]:
            R = M - 1
        else:
            L = M + 1

    return False

a = [10, 20, 30, 40, 50]
print(Search(a,20))