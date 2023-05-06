class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    pop = stack.pop()
                    if (i==')' and pop !='('):
                        return False
                    elif (i=='}' and pop !='{'):
                        return False
                    elif (i==']' and pop !='['):
                        return False
        if len(stack)>0:
            return False
        else:
            return True
