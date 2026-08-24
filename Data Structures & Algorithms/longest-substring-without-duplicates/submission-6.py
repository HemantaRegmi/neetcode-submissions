class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l) #updates the latest instance of the repeating char
            mp[s[r]] = r #saves where the current character was last seen
            res = max(res, r - l + 1) #saves max substring length
        return res
