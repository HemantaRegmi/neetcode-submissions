class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        const counter = new Map()

        let maxStr = 1
        let l = 0
        let r = 0

        if (s === "") {
            
            return 0;
        }


        while(r < s.length) {
        if (counter.has(s[r])) {
            counter.delete(s[l]);
            l++;
        } else {
            counter.set(s[r]);
            maxStr = Math.max(maxStr, r - l + 1);
            r++;
        }
            
        }
        return maxStr
    }
}
