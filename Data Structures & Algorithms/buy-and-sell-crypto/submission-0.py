class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0

        for price in prices:
            profit = price - lowest_price

            if profit > max_profit:
                max_profit = profit

            if price < lowest_price:
                lowest_price = price

        return max_profit