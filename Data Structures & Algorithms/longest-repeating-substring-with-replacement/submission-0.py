class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # stores needed characters
        res = 0 #max of the longest window found

        l = 0 #left pointer
        maxf= 0 #stores highest frequency
        for r in range(len(s)): #goes through string with r pointer
            count[s[r]] = 1 + count.get(s[r], 0) #count of the current char gets added to its occurences already in the dict. if not there then 0
            maxf = max(maxf, count[s[r]]) #captures longest frequency

            while (r-l +1) - maxf > k: #while window - max frequecy of chars is greater than k
                count[s[l]] -=1 #reduces char
                l+=1 #moves window forward
            res = max(res,r-l+1)
        return res

