class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lower = 0
        higher = 0
        length = len(nums)
        for i in nums:
            if i < target:
                lower += 1
            elif i > target:
                higher += 1
        return [i for i in range(lower, length - higher)]