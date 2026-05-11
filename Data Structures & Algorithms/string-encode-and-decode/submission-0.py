class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #this is where our encoded string will be saved
        for s in strs:
            res += str(len(s)) + "#" + s #adds the numerical length of the string as a string. Adds the encoded hash symbol and then the string itself 
        return res

    def decode(self, s: str) -> List[str]:
        res, i=[], 0 #res has the encoded string, i=[] is where the decoded string will be, 0 track encoded
        while i < len(s):
            j = i # another pointer j to find #
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) #Gathers window of string before # which is the number and converts to int
            res.append(s[j+1 : j+1+length]) #grabs instance string after # j+1 to the end j+1+length
            i = j+1+length #add the string to the final decoded array
        return res


