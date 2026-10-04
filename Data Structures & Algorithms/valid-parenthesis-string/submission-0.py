class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin, leftmax = 0, 0

        for a in s:
            if a =="(":
                leftmin = leftmin +1
                leftmax = leftmax +1
            elif a ==")":
                leftmin = leftmin-1
                leftmax = leftmax-1
            else:
                leftmin = leftmin-1
                leftmax = leftmax+1
            if leftmax<0:
                return False
            if leftmin<0:
                leftmin = 0
        return leftmin == 0
