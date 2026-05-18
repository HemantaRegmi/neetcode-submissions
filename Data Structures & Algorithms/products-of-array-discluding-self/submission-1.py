class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) #multiplying makes it to where the length of the res array will be length of nums
        prefix = 1
        postfix = 1

        for i in range(len(nums)): #looping through nums
            res[i] = prefix #where all the values of products will be placed before the last element in the array
            prefix *= nums[i]
        
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res


        