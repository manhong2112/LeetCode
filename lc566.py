class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        res = [[0 for x in range(c)] for y in range(r)]
        for i in range(0, r * c):
            res[i // c][i % c] = nums[i // len(nums[0])][i % len(nums[0])]
        return res
