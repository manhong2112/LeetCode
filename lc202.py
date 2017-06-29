class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = set()
        while n not in x:
            x.add(n)
            n = sum(int(x) ** 2 for x in str(n))
        return n == 1