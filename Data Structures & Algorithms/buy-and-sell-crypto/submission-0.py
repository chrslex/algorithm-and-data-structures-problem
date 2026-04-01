class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_minimum = 101

        for price in prices:
            if price < current_minimum:
                current_minimum = price
                continue
            max_profit = max(max_profit, price-current_minimum)


        return max_profit