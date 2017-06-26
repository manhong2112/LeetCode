class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.lower() == word or (word[0] == word[0].upper() and word[1:] == word[1:].lower()) or word.upper() == word