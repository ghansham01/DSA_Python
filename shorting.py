# Binary Search
# Time Complexity :- O(N^2)
# Space Complexity:- O(1) 

A = [-5,1,2,-3,-4,4,3,5,6]

def bubble_short(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if arr[1-i] > arr[i]:
                