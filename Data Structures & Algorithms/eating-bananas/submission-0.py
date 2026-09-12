class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lp = 1
        rp = max(piles)
        
        sol = rp

        while lp<=rp:
            mid = (lp+rp)//2
            hours = 0
            for a in piles:
                hours+=math.ceil(a/mid)
            if hours <=h:
                sol = min(sol, mid)
                rp =mid-1
            else:
                lp=mid+1
        return sol