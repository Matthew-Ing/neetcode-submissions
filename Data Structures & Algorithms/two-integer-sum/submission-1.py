class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for a in range(len(nums)):
            for b in range(len(nums)):
                print(nums[a] + nums[b])
                if a != b and nums[a] + nums[b] == target:
                    result = [a, b]
                    return result
        return [0]