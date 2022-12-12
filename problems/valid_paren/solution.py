class Solution:

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