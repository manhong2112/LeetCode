class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
            return (ord(s[0]) - 64) * (26 ** (len(s) - 1)) + self.titleToNumber(s[1:])
        else:
            return 0