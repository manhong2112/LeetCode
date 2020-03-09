class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        res = 0
        for i in s:
            if i == "R":
                c += 1
            else:
                c -= 1
            if c == 0:
               res += 1
        return res
