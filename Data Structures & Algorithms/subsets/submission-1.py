class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index: int, path: List[int]):
            result.append(list(path))

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
            
        backtrack(0, [])
        return result
