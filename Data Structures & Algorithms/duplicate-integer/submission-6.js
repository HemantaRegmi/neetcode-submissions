class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const storage = {}
        for(let num of nums) {
            if(num in storage) return true;

            storage[num] = num

        }
        return false;
    }
}
