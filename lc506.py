class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        k = sorted(nums)[::-1]
        d = dict(zip(k[:3], ["Gold Medal", "Silver Medal", "Bronze Medal"]))
        return list(map(lambda x: d[x] if x in d else str(k.index(x) + 1), nums))