class Solution {
public:
    bool function(string a, string b, int i){
        for(int j = 0; j<b.size(); j++){
            if(a[i+j]!=b[j]) return false;
        }
        return true;
    }
    int strStr(string haystack, string needle) {
        for(int i=0;i<haystack.size();i++){
            if(function(haystack,needle,i)) return i;
        }
        return -1;
    }
};