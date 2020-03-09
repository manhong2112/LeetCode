class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        g = {}
        res = []
        for (i, s) in enumerate(groupSizes):
            if s in g:
                g[s].append(i)
            else:
                g[s] = [i]
            if len(g[s]) == s:
                res.append(g[s])
                del g[s]
        return res
