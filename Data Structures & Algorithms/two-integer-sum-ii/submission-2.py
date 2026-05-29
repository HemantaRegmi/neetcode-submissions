class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        closing = []
        for i in numbers:
            for j in numbers:
                if i + j == target:
                    closing.append(numbers.index(i) + 1)
                    closing.append(numbers.index(j) + 1)
                    return closing
        return closing.append(0)