# Two Sum

```
Author: Taylor Sattenfield
Date: 11 December 2022
```

## Problem

Given an array of integers ```nums``` and an integer ```target```, return indices of the two numbers <i>such that they add up to ```target```.</i>

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Example 1:

```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:

```
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

### Example 3:

```
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

Constraints:<br>

```2 <= nums.length <= 10^4```<br><br>
```-10^9 <= nums[i] <= 10^9```<br><br>
```-10^9 <= target <= 10^9```<br><br>
```Only one valid answer exists```<br><br>

# Explanation

Brute-force:<br>
``` python3
def twoSumBrute(self, pList: list[int], pTarget: int) -> list[int]:
    for i in range(0, len(pList)):
        comp = pTarget - pList[i]
        for j in range(i, len(pList)):
            if comp == pList[j] and i != j:
                return [i, j]
```
The time complexity of the brute-force approach is ```O(n^2)```. The idea is to have two loops: outer loop iterates over the entire list and computes a complement value ```comp```, while the inner loop compares the ```comp``` value to each element in ```pList```. If a match is found, ```return [i, j]```, which are the indices of each of the elements that satisfy the ```comp``` condition. One of the constraints given for this problem is there will always be a match, so we don't have to handle the case where there isn't one.

Hashmap / Dictionary:<br>
``` python3
def twoSum(self, pList: list[int], pTarget: int) -> list[int]:
    compDict = {}
    for i in range(0, len(pList)):
        comp = pTarget - pList[i]
        if pList[i] in compDict:
            return [compDict[pList[i]], i]
        else:
            compDict[comp] = i
```
The time complexity of the hashmap / dictionary approach above is ```O(n)```, which is much better than the brute-force algo as we only traverese the dictionary containing ```n``` elements once. Space complexity: ```O(n)```. The extra space required depends on the number of items stored in the hash table, which stores at most ```n``` elements.
