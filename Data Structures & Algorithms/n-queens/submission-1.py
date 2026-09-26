class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def valid(r, c):
            for row in range(r):
                if board[row][c] == "Q":
                    return False
            
            
            row = r - 1
            col = c - 1

            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                
                row -= 1
                col -= 1
            
            row = r - 1
            col = c + 1
            
            while row >= 0 and col < n:
                if board[row][col] == "Q":
                    return False
                
                row -= 1
                col += 1
            
            return True
        

        def solver(r):
            if r == n:
                ans = ["".join(i) for i in board]
                res.append(ans)
                return 
            
            for c in range(n):
                if valid(r, c):
                    board[r][c] = "Q"
                    solver(r + 1)
                    board[r][c] = "."

        
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        solver(0)

        return res