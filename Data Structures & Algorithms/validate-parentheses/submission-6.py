class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')': '(', '}': '{', ']': '['}
        t = []

        if len(s) ==  0:
            return True
            
        for a in s:
            if a in valid.values():
                t.append(a)
                print("pushed", a)
            elif a in valid.keys():
                if t and t[-1] == valid.get(a, 0):
                    print(t.pop())
                else:
                    return False
        if len(t) >0:
            return False
        return True