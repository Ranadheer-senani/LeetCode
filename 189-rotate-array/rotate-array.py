class Solution:
    def rotate(self, a: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(a) - k % len(a)

        a[:] = a[k:] + a[:k]