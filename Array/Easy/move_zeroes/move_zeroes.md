# Move Zeroes

```
Author: Taylor Sattenfield
Date: 24 December 2022
```

## Problem

Given an integer array ```nums```, move all ```0```'s to the end of it while maintaining the relative order of the non-zero elements.

<b>Note</b> that you must do this in-place without making a copy of the array.

### Example 1:

```
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```
### Example 2:

```
Input: nums = [0]
Output: [0]
```

Constraints:<br>

```1 <= nums.length <= 10^4```<br><br>
```-2^31 <= nums[i] <= 2^31 - 1```<br><br>

# Explanation

<ul>
<li>If the input array's length is less than or equal to 1, return the array because no work is needed
<li>Else, we can loop through the array and for every 0 we'll remove it and append it to the array
</ul>

``` python3
class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            [nums]
        for i in range(0, len(nums)):
            if nums[i] == 0 and i != len(nums):
                nums.remove(0)
                nums.append(0)
```
