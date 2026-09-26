class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[idx]:
                idx += 1
                temp = board[r][c]
                board[r][c] = "@"
                res = (dfs(r + 1, c, idx) or dfs(r - 1, c, idx) or dfs(r, c + 1, idx) or dfs(r, c - 1, idx))
                board[r][c] = temp
                return res
            else:
                return False


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False
            