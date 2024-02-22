class Solution:
    def findJudge(self, n: int, trust: List[List[int]]):
        trustout = [0] * n
        trustin  = [0] * n
        for i in trust:
            trustout[i[0]-1] += 1
            trustin[i[1]-1]  += 1
        for i in range(n):
            if trustout[i] == 0 and trustin[i] == n-1:
                return i+1
        return -1