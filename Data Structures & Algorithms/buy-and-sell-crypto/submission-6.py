class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        maxProfit = 0

        for sell in prices:
            if sell < buy:
                buy = sell
            else:
                maxProfit = max(maxProfit, sell - buy)
        
        return maxProfit