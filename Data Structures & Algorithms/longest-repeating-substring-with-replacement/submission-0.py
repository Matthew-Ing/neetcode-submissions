class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        long  = 0

        for r in range(len(s)):

            count[s[r]] = 1+ count.get(s[r], 0)
            while (r-l+1) > k + max(count.values()):
                count[s[l]] -= 1
                l +=1
            long = max(long, r-l+1)
        return long