class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        c = m + n -1
        while (i >= 0 and j >= 0):
            if a[i] > b[j]:
                a[c] = a[i]
                i -= 1
            else:
                a[c] = b[j]
                j -= 1
            c -= 1
        while j >= 0:
            a[c] = b[j]
            j -= 1
            c -= 1
            