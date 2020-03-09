import bisect

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = list([(0, i) for i in range(len(mat[0]))]) + \
            list([(i, 0) for i in range(1, len(mat))])
        for k in m:
            a = []
            for i in range(min(len(mat[0]), len(mat))):
                x, y = k[0] + i, k[1] + i
                try:
                    # it is a bit meanless to use bisect while we can sort directly...
                    bisect.insort(a, mat[x][y])
                except IndexError:
                    break
            for i in range(min(len(mat[0]), len(mat))):
                x, y = k[0] + i, k[1] + i
                try:
                    mat[x][y] = a[i]
                except IndexError:
                    break
        return mat
