class Solution:
    def majorityElement(self, a: List[int]) -> int:
        cand  = a[0]
        votes = 0
        for i in a:
            if votes == 0:
                cand = i
            if cand == i:
                votes += 1
            else:
                votes -= 1
        return cand