class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        trackerS = {}
        trackerT = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            trackerT[t[i]] = 1 + trackerT.get(t[i],0)
            trackerS[s[i]] = 1 + trackerS.get(s[i],0)

        

        return trackerT == trackerS

        