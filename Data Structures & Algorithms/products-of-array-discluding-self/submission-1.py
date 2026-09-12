class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)-1
        pre = {}
        post = {}
        tot = {}

        for a in range(len(nums)):
            # pre
            if a>0:
                pre[a] = nums[a-1] * pre.get(a-1, 1)
            else:
                pre[a] = 1
            # print(pre[a])
            
            # post
            if a>0:
                post[length-a] = nums[length-a+1] * post.get(length-a+1, 1)
                # print(a, length-a, post[length-a])
            else:
                post[length-a] = 1
                # print(length-a)

            # print(length-a, post[length-a])
            
        for b in range(len(nums)):
            tot[b] = pre[b] * post[b]
            print(b, pre[b], post[b], tot[b])

        # print(tot)

        return list(tot.values())