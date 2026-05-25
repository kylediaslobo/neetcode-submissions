class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0
        profit = 0
        
        for i in range(len(prices)):
            j=len(prices)-1
            while j > i:
                if prices[j]-prices[i] > profit:
                    profit = prices[j] - prices[i]
                j-=1
        return profit