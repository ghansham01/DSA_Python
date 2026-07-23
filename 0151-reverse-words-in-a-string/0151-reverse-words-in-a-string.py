class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split()
        split.reverse() 

        return " ".join(split)