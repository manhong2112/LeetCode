class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return list(map(lambda x: 
                            str(x) if not (x % 3 == 0 or x % 5 == 0)
                            else (("Fizz" if x % 3 == 0 else "") + ("Buzz" if x % 5 == 0 else "")),
                        range(1, n+1)))