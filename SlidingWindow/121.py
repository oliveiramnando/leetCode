class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_buy = prices[0]
        
        for i in range(len(prices)):
            min_buy = min(prices[i], min_buy)
            profit = prices[i] - min_buy
            max_profit = max(profit, max_profit)
            
        return max_profit
