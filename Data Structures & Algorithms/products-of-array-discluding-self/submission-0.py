class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        preproduct = 1
        postfix = [1] * len(nums)
        postproduct = 1
        final = [1] * len(nums)

 
        for a in range(len(nums)-1):
            preproduct *= nums[a]
            prefix[a] = preproduct


        for b in range(len(nums)-1, -1, -1):
            postproduct *= nums[b]
            postfix[b] = postproduct


        for i, c in enumerate(nums):
            if i < len(nums)-1:

                final[i] = prefix[i-1] * postfix[i+1]
                print(prefix[i-1])
                print(postfix[i+1])

            else: 
                final[i] = prefix[i-1]
        return final
