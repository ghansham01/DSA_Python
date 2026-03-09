class solution:
    def mergeStrings(word1, word2):

        result = []
        i, j = 0,0
        n=len(word1)
        m = len(word2)

        while i<n and j<m:
            result.append(word1[i])
            result.append(word2[j])

            i+=1
            j+=1

        if i<n:
            result.append(word1[i:])
        
        if j<m: 
            result.append(word2[j:])


        return "".join(result)
    

w1 = "abc"
w2 = "pqr"    

sol = solution
print(sol.mergeStrings(w1, w2))