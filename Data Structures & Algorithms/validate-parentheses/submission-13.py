class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False

        stack = []

        valid = {'}': '{', ')': '(', ']': '['}

        for a in s:
            if a in valid.values():
                stack.append(a)
            elif a in valid.keys() and stack:
                if stack[-1] == valid.get(a):
                    stack.pop()
                    continue
                else:
                    return False
            else:
                return False
        
        if stack:
            return False
        else:
            return True