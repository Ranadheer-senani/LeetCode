from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x = bisect_left(nums,target)
        if x == len(nums) or nums[x] != target: return [-1,-1]
        y = x
        while y<len(nums) and nums[y] == target: y+=1
        return [x,y-1]