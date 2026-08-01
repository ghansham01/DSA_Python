class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        left = 0
        zero = 0
        maximum = 0

        for i in range(n):
            if nums[i]==0:
                zero+=1
            
            while zero>1:
                if nums[left] == 0:
                    zero-=1
                
                left+=1
            
            maximum = max(maximum, i-left)
        
        return maximum