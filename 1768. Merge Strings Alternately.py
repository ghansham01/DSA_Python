class Solution:
    def MergeStringsAlternately(self, word1, word2):
        result = []

        j=0
        i=0
        n = len(word1)
        m = len(word2)

        while i < n and j < m:
            result.append(word1[i])
            result.append(word2[j])

            j+=1
            i+=1

        if i < n:
            result.append(word1[i:])
        
        if j < m:
            result.append(word2[j:])

        return "".join(result)

sol = Solution()
print(sol.MergeStringsAlternately("abc", "pqr"))   
print(sol.MergeStringsAlternately("ab", "pqrs"))