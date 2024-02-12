class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        delaware = []
        for i in range(1,len(a)-1):
            if a[i-1] == a[i+1]:
                delaware.append(i+1)
        for i in delaware[::-1]:
            del a[i]
        return len(a)