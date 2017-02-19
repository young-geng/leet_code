# https://leetcode.com/problems/fizz-buzz/?tab=Description

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return map(self.to_string, xrange(1, n+1))

    def to_string(self, number):
        if number % 15 == 0:
            return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"
        return str(number)
