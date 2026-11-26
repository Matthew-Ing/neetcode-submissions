class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        CS = set()

        Max = 0
        left = 0

        for right in range(len(s)):
            while s[right] in CS:
                
                CS.remove(s[left])
                left+=1
            CS.add(s[right])
            Max = max(Max, right-left+1)
        return Max