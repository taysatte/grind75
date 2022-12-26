
from typing import List

class Solution:
    def max_profit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                p_profit = prices[right] - prices[left]
                max_profit = max(max_profit, p_profit)
            else:
                left = right
            right += 1
        return max_profit