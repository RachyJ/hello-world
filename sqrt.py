# https://leetcode.com/problems/sqrtx/description/

import math

class Solution(object):
    def __init__(self):
        self.value = ''

    def mySqrt(self,x):
        """
        :type x: int
        :rtype: int
        """
        self.value = x
        s = int(math.sqrt(self.value))
        print(s)

a = Solution()

try:    
    i = int(input("Input a number to calculate square foot >"))
    a.mySqrt(i)
except:
    print("Please input an int!")
