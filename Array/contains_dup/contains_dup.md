# Contains Duplicate

```
Author: Taylor Sattenfield
Date: 24 December 2022
```

## Problem

Given an integer array ```nums```, return ```true``` if any value appears <b>at least twice</b> in the array, and return ```false``` if every element is distinct.

### Example 1:

```
Input: nums = [1, 2, 3, 1]
Output: true
```
### Example 2:

```
Input: nums = [1, 2, 3, 4]
Output: false
```
### Example 2:

```
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
```

Constraints:<br>

```1 <= nums.length <= 10^5```<br><br>
```-10^9 <= nums[i] <= 10^9```<br><br>

# Explanation

<ul>
<li>Store each element as a key and its number of ocurrences as a value in a dictionary
<li>Return true if the value is >= to 2 (meaning there is a duplicate element)
</ul>Or return false if each value is <= 2 (meaning each element is unique)

``` python3
class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        counts = Counter(nums).most_common() [0][1]
        return True if counts >= 2 else False
```
