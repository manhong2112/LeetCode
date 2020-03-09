class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        def highestRow(n):
            return max(grid[n])

        def highestCol(n):
            return max([r[n] for r in grid])

        def maxHeight(x, y):
            return min(highestRow(x), highestCol(y))

        return sum(sum(maxHeight(x, y) - v for (x, v) in enumerate(r)) for (y, r) in enumerate(grid))
