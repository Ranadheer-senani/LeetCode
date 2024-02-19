class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sumd(z):
            return sum([int(i) for i in str(z)])
        dct = dict()
        maxFreq = 1
        for i in range(1,n+1):
            dsum = sumd(i)
            if dsum in dct:
                dct[dsum] += 1
                maxFreq = max(maxFreq,dct[dsum])
            else:
                dct[dsum] = 1
        return len([i for i in dct.keys() if dct[i]==maxFreq])