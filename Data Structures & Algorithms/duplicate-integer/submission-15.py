class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        HS = set()

        for a in nums:
            if a in HS:
                return True
            else:
                HS.add(a)
        return False