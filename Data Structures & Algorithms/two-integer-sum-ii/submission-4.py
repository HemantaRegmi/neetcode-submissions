class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        closing = {}
        for i, j in enumerate(numbers):
            complement = target - j
            if complement in closing:
                return [closing[complement] +1, i +1]
            closing[j] = i
        return [0]
