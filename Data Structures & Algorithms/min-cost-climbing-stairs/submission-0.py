class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if(n < 2):
            return min(cost)

        dp = [0 for _ in range(n)]
        dp[n-1] = cost[n-1]
        dp[n-2] = cost[n-2]

        for i in range(n-3, -1, -1):
            dp[i] += cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])
