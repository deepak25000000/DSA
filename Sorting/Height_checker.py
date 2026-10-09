class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        n = len(heights)
        expected = sorted(heights)
        count = 0
        for i in range(0, n):
            if heights[i] != expected[i]:
                count = count + 1
        return count
            
