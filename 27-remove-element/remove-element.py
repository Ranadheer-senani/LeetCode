import copy
class Solution:
    def removeElement(self, a: List[int], v: int) -> int:
        d = dict()
        c = len(a)
        z = copy.deepcopy(a)
        for i in z:
            if i not in d.keys():
                d[i] = 0 
            d[i] += 1
        if v not in d.keys(): return c
        for i in range(d[v]):
            a.remove(v)
        return c - d[v]