class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return '-' + self.convertToBase7(-num)
        elif num < 7:
            return str(num)
        else:
            return self.convertToBase7(num // 7) + str(num % 7)