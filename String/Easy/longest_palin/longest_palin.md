# Longest Palindrome

```
Author: Taylor Sattenfield
Date: 26 December 2022
```

## Problem

Given a string ```s``` which consists of lowercase or uppercase letters, return the <i>length of the <b>longest palindrome</b></i> that can be built with those letters.

Letters are <b>case sensitive</b>, for example, ```"Aa"``` is not considered a palindrome here.

### Example 1:

```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
```

### Example 2:

```
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
```

Constraints:<br>

```1 <= s.length <= 2000```<br><br>
```s consists of lowercase and/or uppercase English letters only.```<br><br>


# Explanation

<ul>
<li>
</ul>


``` python3
class Solution:
    def longest_palindrome(self, s: str) -> int:
        c = Counter(s)
        output = 0

        for count in c.values():
            output += int(count / 2) * 2
            if output % 2 == 0 and count % 2 == 1:
                output += 1
        return output
```
