# https://leetcode.com/problems/sparse-matrix-multiplication/?tab=Description
"""
The optimized solution uses a single hashtable to keep track of the
values in rows of A that are non-zero.

cache[i]-->[a, b,...,e] refers to A[i][j] where A[i][j] is non-zero.

"""



from collections import defaultdict

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        M, N, D = len(A), len(A[0]), len(B[0])
        # result is of shape MxD
        result = [[0 for x in xrange(D)] for x in xrange(M)]
        cache = defaultdict(list)
        for i in range(M):
            for j in range(N):
                # add only non-zero values to our hashtable.
                if A[i][j] != 0:
                    cache[i].append(j)

        for i in range(M):
            for k in range(D):
                val = 0
                for col in cache[i]:
                    val = val + A[i][col]*B[col][k]
                result[i][k] = val
        return result

    def dumb_multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        def multiply_helper(i, j):
            total = 0
            for k in xrange(N):
                total += A[i][k] * B[k][j]
            return total

        M = len(A)
        N = len(A[0]) # must equal len(B)
        D = len(B[0])

        assert N == len(B)
        # output is of shape MxD
        result = [[0 for x in xrange(D)] for x in xrange(M)]

        for i in xrange(M):
            for j in xrange(D):
                result[i][j] = multiply_helper(i, j)
        return result
