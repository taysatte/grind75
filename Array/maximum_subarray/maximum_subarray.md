# Maximum Subarray

```
Author: Taylor Sattenfield
Date: 10 January 2023
```

## Problem

Given an integer array `nums`, find the <i>subarray</i> with the largest sum, and return its sum.

### Example 1:

```
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum 6.
```
### Example 2:

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```
### Example 3:

```
Input: nums = [5, 4, -1, 7, 8]
Output: 23
Explanation: The subarray [5, 4, -1, 7, 8] has the largest sum 23.
```

Constraints:<br>

```1 <= prices.length <= 10^5```<br><br>
```0 <= prices[i] <= 10^4```<br><br>

# Explanation

<ul>
<li>
</ul>

``` python3
class Solution:
    def max_subarray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        curr_sum = 0
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_sub = max(max_sub, curr_sum)
        return max_sub
```
