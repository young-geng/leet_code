# https://leetcode.com/problems/longest-absolute-file-path/
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen = 0
        parent_pathlen = {0:0}
        lines = input.split('\n')
        for line in lines:
            name = line.lstrip('\t')
            # depth is the number of tabs
            depth = len(line) - len(name)
            # check if the name is a filename, if so update the maxlen
            if "." in name:
                maxlen = max(maxlen, parent_pathlen[depth] + len(name))
            # if name is a dir, then update the pathlenByDepth
            else:
                # +1 for / at the end
                parent_pathlen[depth+1] = parent_pathlen[depth] + len(name) + 1
        return maxlen
