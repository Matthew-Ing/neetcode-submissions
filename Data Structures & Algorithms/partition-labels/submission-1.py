class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}

        for i, c in enumerate(s):
            index[c] = i
        sol = []

        size, end = 0, 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, index[c])

            if i == end:
                sol.append(size)
                size = 0
        return sol