# Add Binary

```
Author: Taylor Sattenfield
Date: 28 December 2022
```

## Problem

Given two binary strings ```a``` and ```b```, return <i>their sum as a binary string.</i>

### Example 1:

```
Input: a = "11", b = "1"
Output: "100"
```
### Example 2:

```
Input: a = "1010", b = "1011"
Output: "10101"
```

Constraints:<br>

```1 <= a.length, b.length <= 10^4```<br><br>
```a and b consist only of '0' or '1' characters.```<br><br>
```Each string does not contain leading zeros except for the zero itself.```<br><br>

# Explanation

<ul>
<li>Convert each string into a base 2 integer
<li>Convert those integers back to decimal using bin()
<li>Return the sum of a and b as a string (slicing the '0b' with [2:])
</ul>

``` python3
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))) [2:]
```
