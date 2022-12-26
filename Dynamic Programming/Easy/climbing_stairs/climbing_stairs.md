# Climbing Stairs

```
Author: Taylor Sattenfield
Date: 23 December 2022
```

## Problem

You are climbing a staircase. It takes ```n``` steps to reach the top.

Each time you can either climb ```1``` or ```2``` steps. In how many distinct ways can you climb to the top?

### Example 1:

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

### Example 2:

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

Constraints:<br>

```1 <= ransomNote.length, magezine.length <= 10^5```<br><br>
```ransomNote and magezine consist of lowercase English letters.```<br><br>


# Explanation

<ul>
<li>
</ul>

``` python3
class Solution:
    def climbStairs(self, n: int) -> int:
        num_1, num_2, n_len = 1, 1, n - 1

        for i in range(n_len):
            temp = num_1
            num_1 = num_1 + num_2
            num_2 = temp

        return num_1
```
