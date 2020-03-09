class Solution:

   def searchInsert(self, nums: List[int], target: int) -> int:
      start = 0
      end = len(nums)
      while start < end:
         k = (start + end) // 2
         n = nums[k]
         if target > n:
            start = k + 1
         else:
            end = k
      return start
