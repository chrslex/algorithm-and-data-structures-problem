class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums) if n != 0 else 0
        def helper(part):
            n = len(part)
            memo = [-1 for _ in range(n)]
            

            def dfs(i):
                if i >= n:
                    return 0
                if memo[i] != -1:
                    return memo[i]
                memo[i] = max(part[i] + dfs(i+2), dfs(i+1))
                return memo[i]
            return dfs(0)
        
        return max(helper(nums[:len(nums)-1]), helper(nums[1:]))