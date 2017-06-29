class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = collections.Counter(s).values()
        return sum([x // 2 * 2 for x in k]) + \
                (1 if any([x % 2 == 1 for x in k]) else 0)