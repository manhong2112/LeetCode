class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return list(
            filter(lambda x: set(x.lower()).issubset(set("qwertyuiop")) or 
                             set(x.lower()).issubset(set('asdfghjkl')) or
                             set(x.lower()).issubset(set('zxcvbnm')),
                    words))