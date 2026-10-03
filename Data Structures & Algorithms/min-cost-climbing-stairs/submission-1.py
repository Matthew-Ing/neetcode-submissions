class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for a in range(len(cost)-3, -1, -1):
            cost[a] += min(cost[a+1], cost[a+2])
        
        return min(cost[0], cost[1])