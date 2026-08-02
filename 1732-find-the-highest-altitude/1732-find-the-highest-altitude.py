class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)

        sums = 0
        higistAttitude = 0
        for i in range(0,n):
            sums += gain[i]
            i+=1

            if sums > higistAttitude:
                higistAttitude = sums

        return higistAttitude