# https://leetcode.com/problems/valid-sudoku/

# We are going to have to check row, col and each square starting
# from the top left corner as 0,0 and moving on to each row and column and square
# to keep a HashSet of things we have seen. We will add things as such:
#     * '4' in row 7 will be encoded as "(4)7"
#     * '4' in col 7 will be encoded as "7(4)"
#     * '4' in top-right square is encoded as "0(4)2"
#
#     0_1_2_3_
#     0|
#     1|
#     2|
#
# The good thing about this solution is that with unique row,col and square
# encodings we dont have to keep 3 separate dictionaries for rows, cols and
# squares.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        rows = len(board)
        cols = len(board[0])
        for i in xrange(rows):
            for j in xrange(cols):
                if board[i][j] != '.':
                    kr, kc, kb = self.encode(board, i, j)
                    if kr in seen or kc in seen or kb in seen:
                        return False
                    seen.add(kr)
                    seen.add(kc)
                    seen.add(kb)
        return True

    def encode(self, board, i, j):
        """ returns a tuple of encodings
            one for each row, col, block
        """
        e = "({0})".format(board[i][j])
        row = e + str(i)
        col = str(j) + e
        square = str(i/3) + e + str(j/3)
        return row, col, square
