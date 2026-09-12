class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True
        # else: return False

        lettersS = {}
        lettersT = {}

        if len(s) == 0 or len(t)==0:
            return True
        if len(s) != len(t):
            return False

        for a in range(len(s)):
            lettersS[s[a]] = lettersS.get(s[a], 0) +1
            lettersT[t[a]] = lettersT.get(t[a], 0) + 1
            
        return lettersS == lettersT