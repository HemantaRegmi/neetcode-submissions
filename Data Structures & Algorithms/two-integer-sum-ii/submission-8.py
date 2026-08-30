class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        addSum = 0

        while l < r:
            addSum = numbers[l] + numbers[r]
            if addSum == target:
                return [l+1,r+1]

            elif addSum > target:
                 r -= 1
            elif addSum < target:
                 l += 1
        
        