class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        l=0
        r=n-1
        count = 0

        while l<r:
            res = nums[l]+nums[r]
            if res == k:
                count+=1
                l+=1
                r-=1
            elif res<k:
                l+=1
            
            else:
                r-=1

        return count