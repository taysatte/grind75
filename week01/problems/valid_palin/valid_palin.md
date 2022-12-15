# Valid Palindrome

```
Author: Taylor Sattenfield
Date: 14 December 2022
```

## Problem

A phrase is a <b>palindrome</b> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string ```s```, return ```true``` <i>if it is a palindrome</i>, or ```false``` <i>otherwise.</i>

### Example 1:

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome
```
### Example 2:

```
Input: prices = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome
```
### Example 3:

```
Input: prices = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.
```

Constraints:<br>

```1 <= s.length <= 2 * 10^5```<br><br>
```s consists only of printable ASCII characters```<br><br>

# Explanation

This problem is a great excercise for growing an understanding of string/char operations and how to manipulate them. The idea is to take in a string, convert it to all lowercase letters and determine whether or not it is a valid palindrome. The only trick to it is the handling of non-alphanumeric characters.

There's a couple ways to solve this problem (as goes for all programming problems), but I think the most concise way to approach it is the use of a pointers. This approach consists of a left and right pointer, left starting at the beginning of ```s``` and the right at the end (```len(s) - 1```) of ```s```. The algo is as follows:
<ul>
<li>While <i>left</i> < <i>right</i> loop through <i>s</i>
<li>Check to see if the values at left and right pointers are alphanumeric characters
<li>If the values at left or right pointers aren't alphnumeric, increment or decrement respectively
<li>If the values at each pointer are alphanumeric, compare them to see if they are the same
<li>If the values are not the same, return <i>false</i>, if they are, <i>continue</i>
</ul>
Once the loop reaches the end without kicking out (returning <i>false</i>), the function will return <i>true</i> (<i>s</i> is a valid palindrome).
<br><br>

``` python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.is_alpha(s[left]):
                left += 1
            while left < right and not self.is_alpha(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def is_alpha(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
```
