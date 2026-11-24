class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        left, right =0, len(heights)-1

        while (left<=right):
            currentA = (right-left) * min(heights[left], heights[right])
            maxA = max(currentA, maxA)

            if heights[left]> heights[right]:
                right -=1
            else:
                left+=1
        return maxA