class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        for i in range(len(a)-1,0,-1):
            if a[i] == a[i-1]:
                del a[i]
        return len(a)