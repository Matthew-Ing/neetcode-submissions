class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HM = {}

        for i, a in enumerate(nums):
            b = target - a
            if b in HM.keys():
                c = HM[b]
                return [c, i]
            else:
                HM[a] = i
        return [0]
            