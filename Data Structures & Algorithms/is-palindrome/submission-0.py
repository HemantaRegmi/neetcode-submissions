class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        print(s)
        left = 0
        right = len(s)-1
        while left < right:
            print(s[left])
            print(s[right])
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True
        