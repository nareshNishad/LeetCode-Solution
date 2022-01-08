#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n==1 or n==2:
            return True
        while(n>2):
            if n%2!=0:
                return False
            n = n/2
        return True
        
# @lc code=end

