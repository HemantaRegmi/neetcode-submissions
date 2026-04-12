class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #init for the hash
        freq = [[] for i in range(len(nums) + 1)] #freq captures occurences based on index. The range of this array is established via the loop which captures the length of nums plus one since this input will always be greater than zero

        for n in nums:
            count[n] = 1 + count.get(n, 0) #we begin to cycle through nums. We add 1 for every occurence of the num. If it doesnt exist, we add one to zero

        for n, c in count.items(): #gives us the map
            freq[c].append(n) #we attach the frequencies of the numbers into the index based on the frequency that number showed up as

        res = [] #what will be our return output
        for i in range(len(freq) -1, 0, -1): #starts at the end of the array length of freq for the first part of range, we stop at zero and increment down 1 from the start
            for n in freq[i]: #iterate through freq to append to the return output of highest freq numbers
                res.append(n)
                if len(res) == k: #if the length of res is the same as what k was desired, we have our output
                    return res
                

        

        