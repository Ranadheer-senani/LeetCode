class Solution {
public:
    bool isPal(string s){
        int c = s.size()-1;
        for(int i=0;i<c/2 + 1;i++) if(s[i]!=s[c-i])return false;
        return true;
    }
    string firstPalindrome(vector<string>& words) {
        for (auto i: words)if(isPal(i)) return i;
        return "";
    }
};