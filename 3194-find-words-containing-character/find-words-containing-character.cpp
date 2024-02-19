class Solution {
public:
    bool inline isin(string a, char x){
        for(auto i:a) if(i == x) return true;
        return false;
    }
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> res;
        for(int i=0;i<words.size();i++){
            if (isin(words[i],x))res.push_back(i);
        }
        return res;
    }
};