class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(__import__("functools").reduce(lambda x, y: x ^ ord(y), s + t, 0))