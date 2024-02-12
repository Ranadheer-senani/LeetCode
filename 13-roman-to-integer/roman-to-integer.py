class Solution:
    def romanToInt(self, s: str) -> int:
        d = dict()
        d['I'], d['V'], d['X'], d['L'], d['C'], d['D'], d['M'] = 1,5,10,50,100,500,1000
        val = d[s[-1]]
        for i in range(len(s)-1):
            print(s[i], d[s[i]])
            if d[s[i]] < d[s[i+1]]:
                val -= d[s[i]]
            else:
                val += d[s[i]]
        return val
