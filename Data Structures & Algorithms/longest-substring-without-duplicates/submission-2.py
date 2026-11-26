class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        CS = set()
        
        left = 0
        maxLength = 0

        for right in range(len(s)):
            while s[right] in CS:
                CS.remove(s[left])
                left+=1
            CS.add(s[right])
            maxLength = max(maxLength, right-left+1)
        return maxLength