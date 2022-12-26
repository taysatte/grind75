# Ransom Note

```
Author: Taylor Sattenfield
Date: 22 December 2022
```

## Problem

Given two strings ```ransomNote``` and ```magazine```, return ```true``` if ```ransomNote``` can be constructed by using the letters from ```magazine``` and ```false``` otherwise.

Each letter in ```magazine``` can only be used once in ```ransomNote```.

### Example 1:

```
Input: ransomNote = "a", magazine = "b"
Output: false
```

### Example 2:

```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

### Example 3:

```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

Constraints:<br>

```1 <= ransomNote.length, magezine.length <= 10^5```<br><br>
```ransomNote and magezine consist of lowercase English letters.```<br><br>


# Explanation

<ul>
<li>Initialize a dictionary for storing the characters present in the magazine string.
<li>Loop through the magazine and store each character in our dictionary as the key followed by the amount of times that character occurs as the value.
<li>Loop through the ransomNote string and look up if each character exists in the dictionary
<li>If the character does exist and the character's value != 0, decrement the count of the character in the dictionary
<li>If the character doesn't exist in the dictionary, return false
<li>Return True if every character can be found in the dictionary.
</ul>


``` python3
class Solution:
    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        magDict = dict()
        for s in range(0, len(magazine)):
            magDict[magazine[s]] = magDict.get(magazine[s], 0) + 1
        for i in range(0, len(ransomNote)):
            if ransomNote[i] in magDict.keys() and magDict.get(ransomNote[i]) > 0:
                magDict[ransomNote[i]] = magDict.get(ransomNote[i], 0) - 1
            else:
                return False
        return True
```
