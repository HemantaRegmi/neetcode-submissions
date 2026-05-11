class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #this is where our encoded string will be saved
        for s in strs:
            res += str(len(s)) + "#" + s #adds the numerical length of the string as a string. Adds the encoded hash symbol and then the string itself 
        return res

    def decode(self, s: str) -> List[str]:
        res, i=[], 0 #res is an empty list, i is the pointer to cycle through encoded strings
        while i < len(s):
            j = i # another pointer j to find #
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) #Gathers window of string before # which is the number and converts to int
            res.append(s[j+1 : j+1+length]) #grabs instance string after # j+1 to the end j+1+length and adds it into res
            i = j+1+length #moves pointer to the next encoded string
        return res


