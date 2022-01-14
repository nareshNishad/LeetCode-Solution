#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
from re import T


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        if n%3!=0 or n<3:
            return False
        for i in range(n//3+1):
            if 3**i==n:
                return True
            elif 3**i>n:
                return False
        
        
# @lc code=end

