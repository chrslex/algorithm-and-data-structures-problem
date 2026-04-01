class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 3:
            return max(nums)

        def helper(houses):
            dp = [0 for _ in range(len(houses))]
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                dp[i] = max(houses[i] + dp[i-2], dp[i-1])
            return dp[-1]
        
        return max(helper(nums[0:n-1]), helper(nums[1:]))