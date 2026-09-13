class NumArray:
    def __init__(self, arr):
        self.arr = arr
        self.prefix = [0] * len(arr)
        self.prefix[0] = arr[0]
        for i in range(1, len(arr)):
          self.prefix[i] = self.prefix[i-1] + arr[i] # build the prefix sum array

    def sumRange(self, l, r):
        if l == 0:
          return self.prefix[r]

        return self.prefix[r] - self.prefix[l-1] # sum of elements from index l to r