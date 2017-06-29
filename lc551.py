class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.find("A") == s.rfind("A") and "LLL" not in s