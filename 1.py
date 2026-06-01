def findErrorNums( nums):
    n = len(nums)

    seen = set()
    dup = -1

    for num in nums:
        if num in seen:
            dup = num
        
        seen.add(num)


    miss = -1
    for i in range(1,n+1):
        if i not in seen:
            miss = i

    return [ dup, miss]



nums = [1,2,2,4]

print(findErrorNums(nums=nums))