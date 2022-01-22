class Solution:
    def isValid(self, s: str) -> bool:
        symb = {")":"(","]":"[","}":"{"}
        stack = []
        for i in s:
            if i in symb:
                if stack and stack[-1] == symb[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if len(stack) == 0 else False
