class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        lo, hi = 0, len(heights)-1

        while lo < hi:
            currWater = min(heights[lo], heights[hi]) * (hi-lo)
            maxWater = max(maxWater, currWater)

            if heights[lo] < heights[hi]:
                lo += 1
            else: 
                hi -= 1
        return maxWater
