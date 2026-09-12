class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}

        for a in range(len(s)):
            s_count[s[a]] = 1+ s_count.get(s[a], 0)
            t_count[t[a]] = 1+t_count.get(t[a], 0)
        return s_count == t_count

        return s_count == t_count
            
