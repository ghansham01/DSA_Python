class Solution:
    def maxArea(self, height: List[int]) -> int:
        n= len(height)
        l = 0
        r = n-1

        maximum = 0
        while l<r:
            w= r-l
            h = min(height[l], height[r])

            area = w*h

            maximum = max(maximum, area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return maximum
        