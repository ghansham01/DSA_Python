class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n= len(nums)
        le=0
        zero =0
        maxiumam = 0

        for i in range(n):
            if nums[i] == 0:
                zero+=1

            while zero > k:
                if nums[le] == 0:
                    zero -= 1
                le += 1

            maxiumam = max(maxiumam, i-le+1)

        return maxiumam