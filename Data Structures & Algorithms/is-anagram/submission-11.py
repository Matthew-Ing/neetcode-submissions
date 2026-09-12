class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s.lower()) == sorted(t.lower()):
        #     return True
        # else:
        #     return False

        if len(s) != len(t):
            return False

        cS = {}
        cT = {}

        for a in range(len(s)):
            cS[s[a]] = 1+ cS.get(s[a], 0)
            cT[t[a]] = 1+ cT.get(t[a], 0)

        for b in cS:
            if cS[b] != cT.get(b,0):
                return False

        
        return True