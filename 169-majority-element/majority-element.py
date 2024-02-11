class Solution:
    def majorityElement(self, a: List[int]) -> int:
        d = dict()
        z = a[0]
        for i in a:
            if i not in d:
                d[i] = 0
            d[i] += 1
            if d[z] < d[i]:
                z = i
        return z