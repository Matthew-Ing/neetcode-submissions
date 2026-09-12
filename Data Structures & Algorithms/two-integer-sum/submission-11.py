class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for index, a in enumerate(nums):
            b = target - a
            if b in nums:
                c = nums.index(b)
                if index != c:
                    d= [index, c]
                    return sorted(d)
        
