class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        left_sum = 0

        for i in range(len(nums)):
            # Right Sum = Total Sum - Left Sum - Current Element
            right_sum = total_sum - left_sum-nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1