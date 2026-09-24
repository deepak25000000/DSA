# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ 
''' Leetcode problem 121'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

print(Solution().maxProfit([7,1,5,3,6,4,10,2]))


# Example 1:    
# Input: prices = [7,1,5,3,6,4,10,2]
# Output: 9
# Explanation: Buy on day 2 (price = 1) and sell on day 7 (price = 10), profit = 10-1 = 9.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

