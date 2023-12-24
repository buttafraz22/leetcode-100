class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Two pointer technique, O(n) time.
        
        left, right = 0, 1
        max_diff = 0
        while right < len(prices):
            day_diff = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_diff = max(max_diff, day_diff)
            else:
                left = right
            right += 1
        return max_diff