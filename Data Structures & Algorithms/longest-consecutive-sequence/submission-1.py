class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))

        tracker = 1
        maxTracker = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                tracker += 1
            else:
                tracker = 1

            maxTracker = max(maxTracker, tracker)

        return maxTracker

            
                
        