def isValidSudoku(board):
    # Sets to keep track of seen numbers
    rows = [set() for _ in range(9)]       # one set for each row
    cols = [set() for _ in range(9)]       # one set for each column
    boxes = [set() for _ in range(9)]      # one set for each 3x3 box

    for r in range(9):              
        for c in range(9):          
            num = board[r][c]

            if num == ".":          # skip empty cells
                continue

            # Find which 3x3 box we are in (0–8)
            box_index = (r // 3) * 3 + (c // 3)

            # Check if num already exists in row, column, or box
            if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                return False  # invalid board

            # Otherwise, record the number
            rows[r].add(num)
            cols[c].add(num)
            boxes[box_index].add(num)

    return True  # valid board

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))