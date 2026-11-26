class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        brackets = {')': '(', ']': '[', '}': '{'}

        for a in s:
            if a in brackets.values():
                print("append", a)
                stack.append(a)
            elif stack and a in brackets.keys() and stack[-1] == brackets[a]:
                print("pop ", a)
                stack.pop()
            else:
                print("error")
                return False
        if len(stack) == 0:
            return True
        else:
            return False 