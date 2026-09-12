class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const logger = new Map()

        for(let i=0;i<nums.length; i++) {
            if(logger.has(target - nums[i])) return [logger.get(target-nums[i]),i]

            logger.set(nums[i], i)
        }



    }
}