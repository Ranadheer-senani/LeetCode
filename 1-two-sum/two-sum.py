class Solution:
    def twoSum(self, a: List[int], t: int) -> List[int]:
        d = dict()
        for i,v in enumerate(a):
            if t - v in d:
                return [d[t-v],i]
            d[v] = i
        return [-1,-1]
