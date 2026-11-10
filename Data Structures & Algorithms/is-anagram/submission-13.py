class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterT = {}
        counterS = {}

        if len(s) != len(t):
            return False

        for i, num in enumerate(s):

            counterT[t[i]] = 1 + counterT.get(t[i], 0)
            counterS[s[i]] = 1 + counterS.get(s[i], 0)

        return counterT == counterS



        