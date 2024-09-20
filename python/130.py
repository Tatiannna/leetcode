# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/description/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        num_rows = len(board)
        num_cols = len(board[0])

        
        def dfs(r, c):
            if (r >= 0 and c >= 0 and r < num_rows and c < num_cols and board[r][c] == 'O'):
                board[r][c] = 'T'
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        for row in range(num_rows):
            for col in range(num_cols):
                if (board[row][col] == 'O' and row == 0 or col == 0 or row == num_rows-1 or col == num_cols-1):
                    # board[row][col] == 'T'
                    dfs(row, col)

        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O' 