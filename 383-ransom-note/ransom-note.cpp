class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> rn,mag;
        for(auto i : magazine) mag[i]++;
        for(auto i : ransomNote)rn[i]++;
        for(auto i:rn)if(i.second>mag[i.first]) return false;

        return true;
    }
};