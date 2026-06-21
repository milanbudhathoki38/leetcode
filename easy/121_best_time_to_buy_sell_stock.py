# 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# Topic: Arrays, Greedy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# ----------------------------
# Problem:
# Given an array prices where prices[i] is the stock price on day i,
# find the maximum profit from buying on one day and selling on a
# later day. Only one transaction allowed. Return 0 if no profit
# is possible.
# ----------------------------

# Approach: Track running minimum (Kadane's-family, one pass)
# - min_price = lowest price seen so far (best day to have bought)
# - max_profit = best profit seen so far across all days
# - at each day: check if selling today beats our best profit,
#   THEN update min_price if today is a new low
# Time: O(n) | Space: O(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit_today = prices[i] - min_price
            max_profit = max(max_profit, profit_today)
            min_price = min(min_price, prices[i])

        return max_profit


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    print(f"max_profit = {sol.maxProfit(prices)}")  # max_profit = 5

    prices = [7, 6, 4, 3, 1]
    print(f"max_profit = {sol.maxProfit(prices)}")  # max_profit = 0