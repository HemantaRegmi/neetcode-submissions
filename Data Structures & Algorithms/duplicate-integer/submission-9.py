class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = []

        for num in nums:
            if num in counter:
                return True
            
            counter.append(num)

        return False