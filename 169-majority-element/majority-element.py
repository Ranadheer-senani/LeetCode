class Solution:
    def majorityElement(self, a: List[int]) -> int:
        cand  = a[0]
        votes = 0
        z = len(a)//2
        for i in a:
            if votes == 0:
                cand = i
            votes += 1 if cand == i else -1
            if votes > z:
                return cand
        return cand