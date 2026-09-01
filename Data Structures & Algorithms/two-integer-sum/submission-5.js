class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const logger = new Map()

        for(let i=0;i<nums.length;i++) {
            if (logger.has(target-nums[i])) {
                let firstInd = logger.get(target-nums[i])
                
                return [firstInd,i]
            } else {
                logger.set(nums[i],i)
            }
        }
    }
}
