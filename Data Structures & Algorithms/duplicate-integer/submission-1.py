class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # a = nums[0]
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False