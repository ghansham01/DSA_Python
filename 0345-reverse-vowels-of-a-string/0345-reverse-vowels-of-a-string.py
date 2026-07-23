class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}

        lis = list(s)

        l,r = 0, len(lis)-1

        while l<r:
            while l<r and lis[l] not in vowels:
                l+=1
            while l<r and lis[r] not in vowels:
                r-=1
            
            lis[l],lis[r] = lis[r], lis[l]

            r-=1
            l+=1
        
        return "".join(lis)