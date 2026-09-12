class Solution:
    def hammingWeight(self, n: int) -> int:
        val = 0
        while n:
            val+=n%2
            n=n >> 1
            
        return val