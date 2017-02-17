# https://leetcode.com/problems/happy-number/
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum
# of the squares of its digits, and repeat the process until the number equals 1
# (where it will stay), or it loops endlessly in a cycle which does not include
# 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 19 is a happy number
#
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

"""
We can actually adapt the TORTOISE and HARE algorithm for cycle detection in
Linked Lists to figure this problem out!

The fact is:
If it is a happy number fast pointer and slow pointer will catch up to each other
when the number saturates at 1.

Otherwise, slow pointer and fast pointer will eventually catch up to each other
but the number wont be 1.

So they will both eventually catch up to each other but the value they end up
at will decide everything.
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow, fast = n, self.sum_digit_squares(n)
        while slow != fast:
            slow = self.sum_digit_squares(slow)
            fast = self.sum_digit_squares(self.sum_digit_squares(fast))
        return slow == 1

    def sum_digit_squares(self, n):
        result = 0
        while n:
            ones = n % 10
            result += ones**2
            n /= 10
        return result
