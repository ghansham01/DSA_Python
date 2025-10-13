Nums = [2,7,11,15]
Target = 9
# brute force
# def TowSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] ==target:
#                 return [i, j]
            
def TowSum(nums, target):
    map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map:
            return [map[complement], i]

        map[num] = i

print(TowSum(Nums,Target))