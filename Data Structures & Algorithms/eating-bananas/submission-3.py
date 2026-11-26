class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right    

        while(left<= right):
            mid = (left+right)//2

            time = 0
            for a in piles:
                time += math.ceil(float(a)/mid)

            if h > time:
                res = mid
                right=mid -1
            elif h < time:
                left= mid+1
            else:
                res = mid
                right=mid -1
        return res