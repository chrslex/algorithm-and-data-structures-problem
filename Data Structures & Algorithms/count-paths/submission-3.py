class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i,j):
            if i == 0 or j == 0:
                return 1
                
            if i < 0 or j < 0:
                return 0
            
            if memo[i][j] != 0:
                return memo[i][j]

            memo[i][j] = dfs(i-1,j) + dfs(i, j-1)
            return memo[i][j]
        
        return dfs(m-1,n-1)