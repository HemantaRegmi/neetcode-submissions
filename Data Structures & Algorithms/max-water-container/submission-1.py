class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        totalWater = 0
        maxWater = 0

        while l < r:
            if heights[l] < heights[r]:
                totalWater = (r-l) * heights[l]
                maxWater = max(totalWater, maxWater)
                l+=1

            elif heights[l] > heights[r]:
                totalWater = (r-l) * heights[r]
                maxWater = max(totalWater, maxWater)
                r-=1
            elif heights[l] == heights[r]:
                totalWater = (r-l) * heights[l]
                maxWater = max(totalWater, maxWater)
                r-=1

        return maxWater


        