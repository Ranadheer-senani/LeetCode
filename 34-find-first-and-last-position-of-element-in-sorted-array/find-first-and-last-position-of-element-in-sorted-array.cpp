class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int x = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        if (x >= nums.size() || nums[x] != target) return {-1,-1};
        int y = x;
        while(y<nums.size() && nums[y] == target)y++;
        return {x,y-1};
    }
};