# https://leetcode.com/problems/evaluate-division/

# Algorithm:
# Floyd-Warshall
# Its a variation of Floyd-Warshall where we are computing quotients instead of
# shortest paths. Because an equation A/B = k is like a graph edge A->B with
# edge weight k and reverse is B->A with edge weight 1/k. And a multiplication
# (A/B)*(B/C)*(C/D) is like a path A->B->C->D.

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # floyd-warshal 2D vertex hashtable
        quotients = collections.defaultdict(dict)
        graph = zip(equations, values)
        # fill in the initial values of hashtable
        for vertex_pair, val in graph:
            numer, denom = vertex_pair
            quotients[numer][numer] = 1.0
            quotients[denom][numer] = 1.0
            quotients[numer][denom] = val
            quotients[denom][numer] = 1/val
        # now the beefy part, for all pairs
        # update the shortest distances
        for k in quotients:
            for i in quotients[k]:
                for j in quotients[k]:
                    quotients[i][j] = quotients[i][k] * quotients[k][j]
        return [quotients[numer].get(denom, -1.) for numer, denom in queries]
