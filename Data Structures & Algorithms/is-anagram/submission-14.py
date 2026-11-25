class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        HMOne = {}
        for a in s:
            HMOne[a] = HMOne.get(a, 0)+1


        HMTwo = {}
        for b in t:
            HMTwo[b] = HMTwo.get(b, 0)+1

        return HMOne == HMTwo
            