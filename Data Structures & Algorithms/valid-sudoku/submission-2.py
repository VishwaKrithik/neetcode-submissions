from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board)):

                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                rows[r].append(board[r][c])
                cols[c].append(board[r][c])
                squares[(r//3, c//3)].append(board[r][c])
        
        return True














        # rows = [0] * 9
        # col = [0] * 9
        # squares = [0] * 9

        # for r in range(9):
        #     for c in range(9):
                
        #         if board[r][c] == ".":
        #             continue
                
        #         value = int(board[r][c]) - 1
        #         if ((1 << value) & rows[r]
        #             or (1 << value) & col[c]
        #             or (1 << value) & squares[(r // 3) * 3 + (c // 3)]):
        #             return False
                
        #         rows[r] |= (1 << value)
        #         col[c] |= (1 << value)
        #         squares[(r // 3) * 3 + (c // 3)] |= (1 << value)
            
        # return True

        
        
        # hashset
        """rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                
                if board[r][c] == ".":
                    continue

                if ( board[r][c] in rows[r]
                     or board[r][c] in cols[c]
                     or board[r][c] in squares[(r // 3, c // 3)]):
                     return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c]) 
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True"""