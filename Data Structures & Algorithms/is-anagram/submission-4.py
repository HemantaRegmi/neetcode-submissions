class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checker = list(t)
        if len(s) != len(t):
            return False
        for count in s:
            if count in checker:
                checker.remove(count)
            else:
                return False
        return True
            

        