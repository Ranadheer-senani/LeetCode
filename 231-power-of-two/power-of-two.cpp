class Solution {
public:
    bool isPowerOfTwo(long long n) {
        return ((n==0ll)?0:!(n&(n-1ll)));
    }
};