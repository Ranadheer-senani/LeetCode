class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lower = 0
        ele = 0
        for i in nums:
            if i < target:
                lower += 1
            elif i == target:
                ele += 1
        return list(range(lower, lower + ele))