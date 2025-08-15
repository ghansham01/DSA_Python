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

print(insertionShort(a))