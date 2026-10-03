class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1

        total= 0
        start = 0

        for a in range(len(gas)):
            total += (gas[a]-cost[a])

            if total <0:
                total = 0
                start = a + 1

        return start