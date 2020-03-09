class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join([chr(ord(i) + (ord("a") - ord("A"))) if ord("A") <= ord(i) <= ord("Z") else i for i in str])
