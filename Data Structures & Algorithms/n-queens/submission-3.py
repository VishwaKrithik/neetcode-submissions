class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        rows = cols = n
        res = []
        board = [["." for _ in range(cols)] for _ in range(rows)]
        
        def valid(row, col):
            # No need to check column since dfs parameter is itself column for each traversal

            # Column traversal to check row
            for c in range(col):
                if board[row][c] == "Q":
                    return False
            
            # Lower left diagonal
            for r, c in zip(range(row, rows), range(col, -1, -1)):
                if board[r][c] == "Q":
                    return False

            # Upper left diagonal
            for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[r][c] == "Q":
                    return False
            
            return True


        def dfs(col):
            if col == cols:
                res.append(["".join(row) for row in board])
                return
            
            for row in range(rows):
                if valid(row, col):
                    board[row][col] = "Q"
                    dfs(col + 1)
                    board[row][col] = "."
        
        dfs(0)
        return res
