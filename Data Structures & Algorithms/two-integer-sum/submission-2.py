class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        log = {}
        for i, num in enumerate(nums):
            desired = target - num
            if desired in log:
                first = log[desired]
                return [first, i]
            log[num] = i

        
        