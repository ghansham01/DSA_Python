bord = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

def solveSudoku(borad):
    def is_valid(r,c,num):
        for i in range(9):
            if borad[r][i]==num:
                return False
        
        for i in range(9):
            if borad[c][i]==num:
                return False
            
        box_row = (r//3)*3
        box_colums = (c//3)*3
        for i in range(3):
            for j in range(3):
                if borad[box_row+i][box_colums+j] == num:
                    return False
        
        return True

    def backtraking():
        for r in range(9):
            for c in range(9):
                if borad[r][c] == ".":   # found empty cell
                    for num in map(str, range(1, 10)):  # try "1" to "9"
                        if is_valid(r, c, num):
                            borad[r][c] = num  # place num
                            if backtraking():
                                return True   # solved
                            borad[r][c] = "." # undo (backtrack)
                    return False  # no number worked, backtrack
        return True  # no empty cells left → solved


    backtraking()


print(solveSudoku(bord))