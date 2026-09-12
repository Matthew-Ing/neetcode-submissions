class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(a.lower() for a in s if a.isalnum())
        left = 0
        right = len(s)-1

        while left<=right:
            if s[left] == s[right]:
                left+=1
                right-=1
                continue
            else:
                return False
        return True