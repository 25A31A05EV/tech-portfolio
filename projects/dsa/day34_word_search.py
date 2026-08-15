"""
LeetCode 79: Word Search
Pattern: Backtracking on Grid

Given an m x n grid of characters and a word, return true if the word
exists in the grid. Letters must be adjacent (horizontally/vertically),
and the same cell cannot be used more than once.
"""

def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(row, col, index):
        if index == len(word):
            return True

        if (row < 0 or row >= rows or
            col < 0 or col >= cols or
            board[row][col] != word[index]):
            return False

        temp = board[row][col]
        board[row][col] = '#'

        found = (backtrack(row+1, col, index+1) or
                 backtrack(row-1, col, index+1) or
                 backtrack(row, col+1, index+1) or
                 backtrack(row, col-1, index+1))

        board[row][col] = temp

        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False


# Test cases
board1 = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
print(exist(board1, "ABCCED"))  # True
print(exist(board1, "SEE"))     # True
print(exist(board1, "ABCB"))    # False