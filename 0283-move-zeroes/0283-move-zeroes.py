class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonzero = 0

        for i in range(0,len(nums)):
            if nums[i]!=0:
                temp = nums[i]
                nums[i] = nums[nonzero]
                nums[nonzero] = temp
                nonzero+=1
            i+=1

        return nums
        