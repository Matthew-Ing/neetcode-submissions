class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        sol = r

        while l<=r:
            mid = (l+r)//2
            print(mid)

            time = 0
            for a in piles:
                time += math.ceil(float(a)/mid)
            if time <= h:
                sol = mid
                r = mid-1
            elif time > h:
                l = mid+1
        return sol
