class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = {}
        d = {}

        for a in s:
            if a in c:
                c[a] = c.get(a)+1
            else:
                c[a] = 1
        for b in t:
            if b in d:
                d[b] = d.get(b)+1
            else:
                d[b] = 1

        if c == d:
            return True
        else:
            return False