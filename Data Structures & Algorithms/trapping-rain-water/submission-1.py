class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1

        leftPillar = height[l]
        rightPillar = height[r]
        water = 0

        while l < r:
            if leftPillar <= rightPillar:
                l += 1
                leftPillar = max(leftPillar, height[l])
                water += leftPillar - height[l]
            else:
                r -= 1
                rightPillar = max(rightPillar, height[r])
                water += rightPillar - height[r]

        return water

        