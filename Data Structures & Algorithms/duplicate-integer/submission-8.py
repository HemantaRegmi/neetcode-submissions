class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = []

        for num in nums:
            if num in checker:
                return True
            else:
                checker.append(num)
            
        return False
        