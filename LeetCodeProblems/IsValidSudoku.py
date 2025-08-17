"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
def isValidSudoku(board) -> bool:
    # Create 3x3 sub-boxes
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue # Skip empty cells
            
            # Check row
            if val in rows[r]:
                return False
            rows[r].add(val)
            
            # Check columns
            if val in columns[c]:
                return False
            columns[c].add(val)
            
            # Check 3x3 sub-box
            box_index = (r // 3) * 3 + (c // 3)
            if val in boxes[box_index]:
                return False
            boxes[box_index].add(val)
    
    return True

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))  # ✅ Output: True
