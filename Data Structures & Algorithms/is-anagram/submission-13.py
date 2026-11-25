class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        HMOne = {}
        for a in s:
            if a in HMOne:
                HMOne[a] = HMOne[a] + 1
            else:
                HMOne[a] = 1


        HMTwo = {}
        for b in t:
            if b in HMTwo:
                HMTwo[b] = HMTwo[b] + 1
            else:
                HMTwo[b] = 1

        if HMOne == HMTwo:
            return True
        else:
            return False