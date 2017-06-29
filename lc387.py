class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        return min([s.index(c) for c in set(s) if s.count(c) == 1] or [-1])
