class Solution {
    /**
     * @param {number[]} arr
     * @return {number[]}
     */
    replaceElements(arr) {
        let n = arr.length
        let ans = []

        let rightMax = -1;

        for(let i=arr.length-1; i>=0;i--) {
            ans[i] = rightMax
            rightMax = Math.max(rightMax, arr[i])
        }
        return ans

     
    }

}
