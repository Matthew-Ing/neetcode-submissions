class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = { "}" : "{", ")": "(", "]" : "["}

        for a in s:
            if a in map:
                if stack and stack[-1] == map[a]:
                    stack.pop()
                else: return False
            else: stack.append(a)
        return True if not stack else False