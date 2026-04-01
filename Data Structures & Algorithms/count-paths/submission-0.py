class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0
        def dfs(i, j):
            nonlocal res
            if i >=m or j >=n:
                return
            if i == m-1 and j == n-1:
                res += 1
            directions = [[0,1], [1,0]]

            for direction in directions:
                dfs(i+direction[0], j+direction[1])
        
        dfs(0,0)
        return res