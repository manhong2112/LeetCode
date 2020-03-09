class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(sum(1 for i in r if i < 0) for r in grid)
