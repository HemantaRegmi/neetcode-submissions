class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length) {
            return false;
        }

        const sLog = {}
        const tLog = {}

        for(let i=0; i<s.length; i++) {
            sLog[s[i]] = (sLog[s[i]] || 0) + 1
            tLog[t[i]] = (tLog[t[i]] || 0) + 1 


        }
        for(let key in sLog) {
            if(sLog[key] !== tLog[key]) return false; 
        }
        return true;

}
}