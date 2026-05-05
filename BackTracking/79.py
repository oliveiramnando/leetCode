class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        tracked = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if not (0 <= r < ROW) or not (0 <= c < COL) or (r,c) in tracked or board[r][c] != word[i]:
                return False
            
            tracked.add((r,c))
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            tracked.remove((r,c))

            return res

        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0):
                    return True
            
        return False
        
