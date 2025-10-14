def roted(nums):
    n = len(nums)
    k %= n

    # first loop
    start = 0
    end = n-1
    while start< end:
        nums[start],nums[end] = nums[end],nums[start]
        start+=1
        end-=1

    # second loop
    start = 0
    end = k-1
    while start< end:
        nums[start],nums[end] = nums[end],nums[start]
        start+=1
        end-=1
    
    # third loop
    start = k
    end = n-1
    while start< end:
        nums[start],nums[end] = nums[end],nums[start]
        start+=1
        end-=1

N = [1,2,3,4,5,6,7]

print(roted(N))