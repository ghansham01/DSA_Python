a = [5, 3, 8, 1]
# Bubble short
# Time Complexity :- O(N^2)
# Space Complexity:- O(1) 
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1]= arr[j+1],arr[j]

    return arr

# print("----the shorting array with help of bubble sort----")
# print(bubble_sort(a))

# Selection short
# Time Complexity:- O(n^2)
# Space Complexity:- O(1)
def SelectionShort(arr):
    n= len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j]<arr[min_index]:
                min_index=j
        
        arr[i], arr[min_index] = arr[min_index],arr[i]
    
    return arr

# SelectionShort(a)
# print(f'this short is using selection short algo {a}')

# Insertion Short
# Time Complexity:- O(n^2)
# Space Complexity:- O(1)
def insertionShort(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(i, 0, -1):
            if arr[j-1]> arr[j]:
                arr[j-1], arr[j]= arr[j],arr[j-1]
            else:
                break

    return arr

# print(insertionShort(a))

# Merge sort
# Time complexity:- O(n log n)
# space complexity:- O(n)
def Merge_sort(arr):
    n = len(arr)
    if n <= 1:   # base case
        return arr
    
    mid = n // 2
    left = Merge_sort(arr[:mid])
    right = Merge_sort(arr[mid:])

    l_len = len(left)
    r_len = len(right)

    sorted_arr = [0] * n
    i = j = k = 0

    # Merge two sorted halves
    while i < l_len and j < r_len:
        if left[i] < right[j]:
            sorted_arr[k] = left[i]
            i += 1
        else:
            sorted_arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining
    while i < l_len:
        sorted_arr[k] = left[i]
        i += 1
        k += 1

    while j < r_len:
        sorted_arr[k] = right[j]
        j += 1
        k += 1

    return sorted_arr

print(f"Merge sort:- {Merge_sort(a)}")