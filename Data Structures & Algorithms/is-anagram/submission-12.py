class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        trackerT = {}
        trackerS = {}

        if len(s) != len(t):
            return False

        for i, num in enumerate(s):
            trackerS[s[i]] = 1 + trackerS.get(s[i], 0)
            trackerT[t[i]] = 1 + trackerT.get(t[i], 0)

        return trackerS == trackerT



        