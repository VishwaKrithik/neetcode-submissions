class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Optimized 2P, DP
        max_profit = 0
        buy = prices[0]

        for sell in prices:
            if buy > sell:
                buy = sell
            else:
                profit = sell - buy
                max_profit = max(max_profit, profit)
        
        return max_profit


        # Sliding window
        '''
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            r += 1
        return max_profit'''


        # Brute Force
        '''max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit'''