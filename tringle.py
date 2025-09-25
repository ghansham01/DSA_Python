def minimumTotal(self, triangle):
    n = len(triangle)

    if n==1:
        return triangle[0][0]
        
    for i in range(n-2,-1,-1):
        for j in range(len(triangle[i])):
            min_below = min(triangle[i+1][j], triangle[i+1][j+1])

            triangle[i][j] += min_below
        
    return triangle[0][0]

triangle_input = [[2],[3,4],[6,5,7],[4,1,8,3]]
result = minimumTotal(triangle_input)
print(f"The minimum path sum is: {result}")