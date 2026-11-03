class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        tracker = {} 

        for i, num in enumerate(nums):
            if target - num in tracker:
                return [tracker[target-num], i]

            
            tracker[num] = i



                

            
        