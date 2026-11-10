class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        buy = prices[0]
        profit = 0

        for price in prices[1:]:
            buy = min(buy, price)
            profit = max(profit, price - buy)

        return profit  