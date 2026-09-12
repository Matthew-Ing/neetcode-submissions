class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stack = []
        
        for i, a in enumerate(temperatures):
            while stack and a > stack[-1][0]:
                stackA, stackI = stack.pop()
                sol[stackI] = (i-stackI)
            stack.append([a, i])
        return sol
            