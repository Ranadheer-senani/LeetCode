class Solution {
public:
    int missingNumber(vector<int>& nums) {
        long long c = nums[0] ^ nums.size();
        for(int i=1;i<nums.size();i++) c  = c ^ nums[i] ^ i;
        return c;
    }
};