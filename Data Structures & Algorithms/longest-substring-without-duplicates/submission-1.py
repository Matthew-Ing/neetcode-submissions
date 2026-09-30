class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sc = set()
        l = 0
        r = 0
        long = 0

        for r in range(len(s)):
            while s[r] in sc:
                sc.remove(s[l])
                l+=1
            sc.add(s[r])
            long = max(long, r-l+1)
        return long