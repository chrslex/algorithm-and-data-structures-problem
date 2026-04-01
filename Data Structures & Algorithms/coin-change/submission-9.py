class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = float("inf")
            for coin in coins:
                if amount-coin >= 0:
                    res = min(res, 1 + helper(amount-coin))
            memo[amount] = res
            return res
        minCoins = helper(amount)
        return minCoins if minCoins != float("inf") else -1
