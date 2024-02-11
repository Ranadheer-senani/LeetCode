class Solution:
    def majorityElement(self, a: List[int]) -> int:
        cand  = a[0]
        votes = 0
        for i in a:
            if votes == 0:
                cand = i
            votes += 1 if cand == i else -1
            if votes > len(a)//2:
                return cand
        return cand