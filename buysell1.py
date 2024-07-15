class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        n = len(prices)
        left = 0
        right = 1 

        while right < n :

            curr = prices[right] - prices[left] 

            if prices[left] < prices[right]:
                profit = max(profit, curr) 
            else:
                left = right 
            right += 1 
        
        return profit 
