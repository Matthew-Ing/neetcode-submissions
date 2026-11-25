class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while(right < len(prices)):
            currentProfit = prices[right] - prices[left]
            if currentProfit<0:
                left = right
            maxProfit = max(maxProfit, currentProfit)
            right+=1
        return maxProfit