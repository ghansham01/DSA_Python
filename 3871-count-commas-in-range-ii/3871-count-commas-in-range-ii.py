class Solution:
    def countCommas(self, n: int) -> int:
        count = 0 
        start = 1000
        comas = 1
        while start<=n:
            end = start * 1000 - 1
            if end > n:
                end = n
            count += (end - start + 1) * comas
            start *= 1000
            comas += 1
        return count