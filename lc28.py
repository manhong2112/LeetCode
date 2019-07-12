class Solution:

   def strStr(self, haystack: str, needle: str) -> int:
      # of course not calling std lib...
      # i don't know why it work, doesn't it same with loop forward?...
      if needle == "":
         return 0
      if len(needle) > len(haystack):
         return -1
      if haystack == needle:
         return 0
      i = 0
      while i < len(haystack):
         if haystack[i] == needle[-1]:
            k = 0
            while True:
               if k == len(needle):
                  print(i)
                  return i - k + 1
               elif i - k < 0 or \
                     len(needle) - k - 1 < 0 or \
                     haystack[i - k] != needle[len(needle) - k - 1]:
                  break
               k += 1
         i += 1
      return -1
