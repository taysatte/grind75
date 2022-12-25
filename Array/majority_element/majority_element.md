# Majority Element

```
Author: Taylor Sattenfield
Date: 24 December 2022
```

## Problem

Given an array ```nums``` of size ```n```, return the <i>majority element</i>.

The majority element is the element that appears more than ```⌊n / 2⌋``` times. You may assume that the majority element always exists in the array.

### Example 1:

```
Input: nums = [3, 2, 3]
Output: 3
```
### Example 2:

```
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
```

Constraints:<br>

```n == nums.length```<br><br>
```1 <= n <= 5 * 10^4```<br><br>
```-10^9 <= nums[i] <= 10^9```<br><br>

# Explanation

Two solutions are provided, one implements a typical looping structure while the other utilizes a more pythonic approach. Both solutions do quite the same thing:

<ul>
<li>Store each element in a dictionary as a key and the frequency as the value
<li>Loop through the keys and check to see which value is larger than (n / 2) (majority element)
</ul>

``` python3
class Solution:
    def majority_element(self, nums: List[int]) -> int:
        num_dict = dict()
        n = len(nums)
        freq = math.floor(n / 2)

        for i in range(n):
            num_dict[nums[i]] = num_dict.get(nums[i], 0) + 1

        for i in num_dict:
            if num_dict[i] > freq:
                return i

    def majority_element_count(self, nums: List[int]) -> int:
        return Counter(nums).most_common() [0][0]
```
