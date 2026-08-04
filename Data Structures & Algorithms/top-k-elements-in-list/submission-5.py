class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        

        for n in nums:
            if n in nums:
                counter[n] += 1
            
        return sorted(counter.keys(), key=counter.get, reverse=True)[:k]

        
        
        
