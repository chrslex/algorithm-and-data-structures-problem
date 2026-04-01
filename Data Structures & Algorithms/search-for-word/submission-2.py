class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ncol = len(board[0])
        nrow = len(board)

        def dfs(r,c,k, visited):
            # edge case 1
            if k == len(word):
                return True
            # edge case 2
            if r < 0 or c < 0 or r >= nrow or c >= ncol or visited[r][c] or board[r][c] != word[k]:
                return False
            
            # mark
            visited[r][c] = True
            # do something
            res = dfs(r+1,c,k+1, visited) or dfs(r-1,c,k+1,visited) or dfs(r,c+1,k+1,visited) or dfs(r,c-1,k+1,visited)
            if res:
                return True
            # backtrack
            visited[r][c] = False
            return False
        
        for i in range(nrow):
            for j in range(ncol):
                if dfs(i,j,0, [[False for _ in range(ncol)] for _ in range(nrow)]):
                    return True
        return False
            