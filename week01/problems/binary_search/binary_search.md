# Binary Search

```
Author: Taylor Sattenfield
Date: 17 December 2022
```

## Problem

Given an array of integers ```nums``` which is sorted in ascending order, and an integer ```target```, write a function to search ```target``` in ```nums```. If ```target``` exists, then return its index. Otherwise, return ```-1```.

You must write an algorithm with ```O(log n)``` runtime complexity.

### Example 1:

```
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```
### Example 2:

```
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

Constraints:<br>

```1 <= nums.length <= 10^4```<br><br>
```-10^4 <= nums[i], target < 10^4```<br><br>
```All the integers in nums are unique```<br><br>
```nums is sorted in ascending order```<br><br>

# Explanation

There are generally two ways to write a binary search algorithm: iteratively or recursively. The main idea behind binary search is:

<ul>
<li>Initialize left and right pointers to point to the beginning and end of the list
<li>While left pointer <= right pointer:
<li>Compute a middle index value and compare that value to our target
<li>If middle value < target: move the left pointer to the middle position index + 1
<li>If middle value > target: move the right pointer to the middle position index - 1
<li>Return -1 if the value is not in the list
</ul>

Here's the iterative approach:

``` python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + math.floor(((right - left) / 2))
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
```