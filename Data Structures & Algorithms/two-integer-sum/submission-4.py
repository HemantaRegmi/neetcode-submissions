class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        secondNum = 0

        for i, num in enumerate(nums):
            secondNum = target - num
            if secondNum in compliment:
                return [compliment[secondNum],i]
            
            compliment[num] = i

                

            
        