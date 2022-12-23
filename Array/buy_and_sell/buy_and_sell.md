# Best Time to Buy and Sell Stocks

```
Author: Taylor Sattenfield
Date: 13 December 2022
```

## Problem

You are given an array ```prices``` where ```prices[i]``` is the price of a given stock on the ```ith``` day.

You want to maximize your profit by choosing a <b>single day</b> to buy one stock and choosing a <b>different day in the future</b> to sell that stock.

Return the <i>maximum profit you can achieve from this transaction.</i> If you cannot achieve any profit, return ```0```.

### Example 1:

```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = (6 - 1) = 5.
(Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell).
```
### Example 2:

```
Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

Constraints:<br>

```1 <= prices.length <= 10^5```<br><br>
```0 <= prices[i] <= 10^4```<br><br>

# Explanation

This problem is great for learning the fundamentals of the sliding window problem solving technique. The algorithm is pretty straight-forward:
<ul>
<li>Establish a left and right pointer to walk down the list
<li>While our right pointer is not at the end of our list we can check to see if the value at our left pointer is greater than the value at our right pointer
<li>If so, we can compute a potential profit (p_profit = prices[right] - prices[left])
<li>If the potential profit is more than our current max, we can update the max_profit variable
<li>If we find that the left pointer is greater than the right pointer we'll "slide" it to our right pointer and increment the right pointer
<li>After our algorithm finishes, we can return the max_profit
</ul>

``` python3
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
```
