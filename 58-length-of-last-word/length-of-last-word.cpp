class Solution {
public:
    int lengthOfLastWord(string s) {
        int size = s.size();
        while(size>=0){
            if(s[size-1] == ' ')size--;
            else break;
        }
        int c = 0;
        for (int i=0;i<size;i++){
            c++;
            if(s[i]==' ')c = 0;
        }
        return c;
    }
};