class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        count = sum(1 for i in range(k) if s[i] in vow)

        maximum = count

        for i in range(k, len(s)):
        # Remove left character
            if s[i - k] in vow:
                count -= 1
        
        # Add right character
            if s[i] in vow:
                count += 1
            
            maximum = max(maximum, count)
        
        return maximum