class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        d = 0
        while len(points) > 1:
            x, y = points[-1]
            a, b = points[-2]
            d += max(abs(x-a), abs(y-b))
            points.pop()
        return d
        