# Valid Anagram

```
Author: Taylor Sattenfield
Date: 16 December 2022
```

## Problem

Given two strings ```s``` and ```t```, return ```true``` <i>if ```t``` is an anagram of</i> ```s```, and ```false``` otherwise.

An <b>Anagram</b> is a word of phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1:

```
Input: s = "anagram", t = "nagaram"
Output: True
```
### Example 2:

```
Input: s = "rat", t = "car"
Output: False
```

Constraints:<br>

```1 <= s.length, t.length <= 5 * 10^4```<br><br>
```s and t consist of lowercase English letters.```<br><br>

# Explanation

So, the python solution to this problem is quite simple due to the nature of the language. The idea is to take both input strings (```s``` and ```t```), sort them in alphabetical order, compare them and return the result. Since an anagram of a word has to contain the all the original letters exactly once, we can just sort the strings to see if they are the same. Here's the solution:

``` python3
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```
