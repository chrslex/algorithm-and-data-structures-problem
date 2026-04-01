class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(temp):
            res = float("inf")

            if temp == 0:
                return 0

            if temp in memo:
                return memo[temp]
            
            for coin in coins:
                if temp-coin >= 0:
                    res = min(res, 1 + dfs(temp-coin))
            memo[temp] = res

            return res 

        res = dfs(amount)

        return res if res < float("inf") else -1