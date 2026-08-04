class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        log = {}
        for i, num in enumerate(nums):
            desired = target - num
            if desired in log:
                matching_index = log[desired]
                return [matching_index, i]
            log[num] =i
        
        