class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        storage = []

        for i, num in enumerate(nums):
            if (target-num) in storage:
                return [storage.index(target-num),i]

            else:
                storage.append(num)




                

            
        