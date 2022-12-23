# First Bad Version

```
Author: Taylor Sattenfield
Date: 19 December 2022
```

## Problem

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have ```n``` versions ```[1, 2, ..., n]``` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API ```bool isBadVersion(version)``` which returns whether ```version``` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

### Example 1:

```
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```
### Example 2:

```
Input: n = 1, bad = 1
Output: 1
```

Constraints:<br>

```1 <= bad <= n <= 2^31 - 1```<br><br>

# Explanation

This problem is a good example of how utilize the binary search algorithm. Since the versions will always be in an ordered configuration we can use binary search:

<ul>
<li>Initialize a left and right pointer to be 0 and n respectively
<li>While the left pointer is less than the right pointer:
<li>Calculate a midpoint value
<li>If the midpoint value isn't bad we update the left pointer to the mid position + 1
<li>If the midpoint value is bad we update the right pointer to the mid value
<li>Once the right pointer overlaps the left, return right (or left)

``` python3
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n

        while left < right:
            mid = int(left + (right - left) / 2)
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return right
```