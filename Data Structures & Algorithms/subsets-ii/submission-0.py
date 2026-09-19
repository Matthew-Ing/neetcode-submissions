class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()


        def dfs(i, curr):
            #  base cases
            if i>=len(nums):
                res.append(curr.copy())
                return
            


            # case 1 with
            curr.append(nums[i])
            dfs(i+1, curr)
            # case 2 w/o
            curr.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1, curr)
        dfs(0, [])
        return res