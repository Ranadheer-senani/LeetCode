class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        int l = 0, t = 0;
        vector<int> res;
        for(int i:nums){
            if(i<target) l++;
            else if(i == target)t++;
        }
        for(int i=l;i<l+t;i++)res.push_back(i);
        return res;
    }
};