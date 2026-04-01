class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return max(nums)

        memo = [0 for _ in range(n)]
        def dfs(i):
            if i >= n:
                return 0
            if memo[i] != 0:
                return memo[i]
            memo[i] = max(dfs(i+1), dfs(i+2) + nums[i])
            return memo[i]
        
        return dfs(0)