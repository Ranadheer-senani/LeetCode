class Solution {
public:
    int minSubArrayLen(int target, vector<int>& a) {
        long long int csum = 0, best = INT_MAX;
        int i = 0;
        for(int j=0; j<a.size(); j++){
            csum += a[j];
            while (csum >= target){
                best = min(best,j-i+1ll);
                csum -= a[i];
                i++;
            }          
        }
        return best==INT_MAX?0:best;
    }
};