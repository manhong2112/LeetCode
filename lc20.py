class Solution:

   def isValid(self, s: str) -> bool:
      l = []
      for i in s:
         if i == "(":
            l.append(")")
         elif i == "{":
            l.append("}")
         elif i == "[":
            l.append("]")
         else:
            if len(l) == 0 or i != l.pop():
               return False
      return len(l) == 0
