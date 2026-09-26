class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        l = 0
        h = len(nums) - 1
        first = -1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                first = mid       
                h = mid - 1       

            elif nums[mid] < target:
                l = mid + 1

            else:
                h = mid - 1

        if first == -1:
            return [-1, -1]

        l = 0
        h = len(nums) - 1
        last = -1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                last = mid
                l = mid + 1

            elif nums[mid] < target:
                l = mid + 1

            else:
                h = mid - 1

        return [first, last]