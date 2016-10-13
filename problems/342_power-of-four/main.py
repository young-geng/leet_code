# https://leetcode.com/problems/power-of-four/
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        mask = int(eval('0b'+'1'+'01'*15)) # 1010101010101010101010101010101
        return num != 0 and num & (num - 1) == 0 and num & mask == num
