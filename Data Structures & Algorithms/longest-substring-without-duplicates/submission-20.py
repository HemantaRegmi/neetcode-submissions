class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        long = 0
        l = 0

        for r, char in enumerate(s):
            if s[r] in mp:
                 l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            long = max(long, r-l+1)
        return long
            

            

