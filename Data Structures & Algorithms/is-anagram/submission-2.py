class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_check = []
        t_check = []

        s_check = sorted(s)
        t_check = sorted(t)

        return s_check == t_check
            
