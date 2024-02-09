class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = 0, j = 0,c=0;
        int a[max(m,1)];
        for (int k = 0;k<m;k++){
            a[k]=nums1[k];
        }
        while(i<m & j<n){
            nums1[c++] = a[i]<nums2[j]?a[i++]:nums2[j++];
        }
        while(i<m){
            nums1[c++] = a[i++];
        }
        while(j<n){
            nums1[c++] = nums2[j++];
        }
    }
};