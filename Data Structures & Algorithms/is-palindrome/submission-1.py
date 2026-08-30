class Solution:
    def isPalindrome(self, s: str) -> bool:
        palinStr = ''
        s = s.lower()
        for c in s:
            if c.isalnum():
                palinStr += c

        return palinStr == palinStr[::-1]
                
        