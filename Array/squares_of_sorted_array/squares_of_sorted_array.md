# Squares of a Sorted Array

```
Author: Taylor Sattenfield
Date: 24 December 2022
```

## Problem

Given an integer array ```nums``` sorted in <b>non-decreasing</b> order, return <i>an array of the squares of each number sorted in <b>non-decreasing</b> order.</i>

### Example 1:

```
Input: nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
Explanation: After squaring, the array becomes [16, 1, 0, 9, 100].
After sorting, it becomes [0, 1, 9, 16, 100].
```
### Example 2:

```
Input: nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]
```

Constraints:<br>

```1 <= nums.length <= 10^4```<br><br>
```-10^4 <= nums[i] <= 10^4```<br><br>
```nums is sorted in non-decreasing order.```<br><br>

# Explanation

<ul>
<li>Initialize a new array to store the squared values
<li>Loop through <i>nums</i>, square each element and append it to the new array
<li>Return the new array sorted in ascending order
</ul>

``` python3
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in range(len(nums)):
            sqr = int(nums[i] * nums[i])
            new_nums.append(sqr)
        return sorted(new_nums)
```
