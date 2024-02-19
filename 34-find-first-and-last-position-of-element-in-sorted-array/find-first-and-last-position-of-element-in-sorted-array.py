from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x = bisect_left(nums,target)
        if x == len(nums) or nums[x] != target: return [-1,-1]
        y = bisect_right(nums, target)-1
        return [x,y]