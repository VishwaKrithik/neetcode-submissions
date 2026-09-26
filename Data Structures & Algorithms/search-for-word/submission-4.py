class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        seen = set()

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[idx] and (r, c) not in seen:
                idx += 1
                seen.add((r, c))
                res = (dfs(r + 1, c, idx) or dfs(r - 1, c, idx) or dfs(r, c + 1, idx) or dfs(r, c - 1, idx))
                seen.remove((r, c))
                return res
            else:
                return False


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    seen = set()
                    if dfs(r, c, 0):
                        return True
        
        return False
            