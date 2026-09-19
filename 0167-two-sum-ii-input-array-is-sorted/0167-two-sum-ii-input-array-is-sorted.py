class Solution:
    def twoSum(self, arr: list[int], index: int) -> list[int]:
        l = 0
        r = len(arr) -1
        result = []

        while l<=r:
            sums = arr[l]+arr[r]
            if sums == index:
                return [l + 1, r + 1]

            elif index > sums:
                l+=1
            else:
                r-=1