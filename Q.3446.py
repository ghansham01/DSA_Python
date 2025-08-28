# def MatrixGrid(grid):
#     n = len(grid)
#     d = {}
#     for i in range(n):
#         for j in range(n):
#             key = i-j
#             if key not in d:
#                 d[key]= []
#             d[key].append(grid[i][j])
#     for key in d:
#         if key >=0:
#             d[key].sort(reverse=True)
#         else:
#             d[key].sort()
#     for i in range(n):
#         for j in range(n):
#             grid[i][j] = d[i-j].pop(0) 
#     return grid


G = [[1,7,3],[9,8,2],[4,5,6]]

# fix = MatrixGrid(G)

def MateixGrid(grid):
    n = len(grid)
    d = {}
    idx = {}

    # Step 1: Collect diagonals
    for i in range(n):
        for j in range(n):
            key = i - j
            if key not in d:
                d[key] = []
                d[key].append(grid[i][j])

    # Step 2: Sort diagonals
    for key in d:
        if key >= 0:   # bottom-left
            d[key].sort(reverse=True)   # non-increasing
        else:          # top-right
            d[key].sort()               # non-decreasing
        idx[key] = 0  # start pointer

    # Step 3: Place values back using index pointers
    for i in range(n):
        for j in range(n):
            key = i - j
            grid[i][j] = d[key][idx[key]]
            idx[key] += 1  # move pointer

    return grid

fix = MateixGrid(G)