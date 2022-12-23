# Valid Parenthesis

```
Author: Taylor Sattenfield
Date: 11 December 2022
```

## Problem

Given a string s containing just the characters ```'('```, ```')'```, ```'{'```, ```'}'```, ```'['``` and ```']'```, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.

### Example 1:

```
Input: s = '()'
Output: True
```

### Example 2:

```
Input: s = '()[]{}'
Output: True
```

### Example 3:

```
Input: s = '(]'
Output: False
```

<br>Constraints:<br>

```1 <= s.length <= 10^4```<br><br>
```s consists of parenthesis only '()[]{}'```<br><br>

# Explanation

This problem is the perfect example of how to use the stack data structure. Basically, the idea is to loop through the string ```s``` and for every "open" bracket ```'('```, ```'['```, ```'{'``` we find, push it onto the stack. We'll also use a dictionary to map the opening and closing bracket pairs together.<br>

Once we come across something other than an opening bracket (closing bracket) ```')'```, ```']'```, ```'}'``` we check to see if it's corresponding opening bracket is at the top of the stack. If the corresponding opening bracket is at the top of the stack, we'll pop that bracket off the top because it's proven to be a valid pair. If isn't at the top of the stack, we'll return ```False``` since this goes against the problem's criteria for a valid parenthesis pair.

Finally, we'll check to see if the stack has any remaining elements left in it, if it does we'll return ```False```, meaning all the brackets did not get closed. If the stack is empty, all of the brackets were closed with their corresponding pair so we can return ```True```.

``` python3
def isValid(self, s: str) -> bool:
    parenDict = {']' : '[', ')' : '(', '}' : '{'}
    stack = []

    for i in range(0, len(s)):

      if len(s) <= 1:
          return False

      if s[i] == parenDict[')']:
          stack.append(s[i])
      elif s[i] == parenDict[']']:
          stack.append(s[i])
      elif s[i] == parenDict['}']:
          stack.append(s[i])
      else:
          if len(stack) > 0 and parenDict[s[i]] == stack[-1]:
              stack.pop()
          else:
              return False

    if len(stack) == 0:
        return True
    return False
```
