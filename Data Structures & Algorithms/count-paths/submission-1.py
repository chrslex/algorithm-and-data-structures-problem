class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i, j):
            res = 0
            if i >=m or j >=n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            directions = [[0,1], [1,0]]

            for direction in directions:
                res += dfs(i + direction[0], j + direction[1])
            return res
        
        res = dfs(0,0)
        return res