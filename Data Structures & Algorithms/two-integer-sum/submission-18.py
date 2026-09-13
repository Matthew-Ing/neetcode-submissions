class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for a,c in enumerate (nums):
            b = target - c
            if b in map: 
                return [map[b],a]
            map[c] = a

        return[0,0]