class Solution:

   def countAndSay(self, n: int) -> str:
      k = "1"
      i = 1
      while i < n:
         i += 1
         k = self.countAndSayNext(k)
      return k

   def countAndSayNext(self, n: int) -> str:
      return "".join(str(len(x)) + str(x[0]) for x in self.groupby(str(n), lambda x, y: x == y))

   def groupby(self, seq, f):
      if seq == []:
         return []
      newseq = [[seq[0]]]
      for i in seq[1:]:
         if f(newseq[-1][0], i):
            newseq[-1].append(i)
         else:
            newseq.append([i])
      return newseq
