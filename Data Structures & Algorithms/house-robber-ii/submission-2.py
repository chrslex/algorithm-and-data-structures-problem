class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n < 3):
            return max(nums)

        def helper(nums):
            nn = len(nums)
            dp = [0 for _ in range(nn)]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, nn):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            
            return dp[-1]
        
        return max(helper(nums[1:]), helper(nums[0:n-1]))
        