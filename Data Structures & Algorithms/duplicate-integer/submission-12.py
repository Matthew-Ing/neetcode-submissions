class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for a in nums:
            before = len(s)
            s.add(a)
            after = len(s)
            if before == after:
                return True
        return False