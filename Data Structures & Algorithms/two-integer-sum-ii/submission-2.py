class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements = defaultdict(int)

        for i in range(len(numbers)):
            temp = target - numbers[i]

            if complements[temp]:
                return [complements[temp], i + 1]
            
            complements[numbers[i]] = i + 1
        return []
