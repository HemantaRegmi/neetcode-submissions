class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const log = new Map()
        for(let i=0; i<nums.length;i++) {
            
            if(log.has(target-nums[i])) {
                return [log.get(target-nums[i]), i]
            } else {
                log.set(nums[i], i)
            }

        }
    }
}