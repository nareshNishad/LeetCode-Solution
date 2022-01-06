#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        a = 1
        b = 2
        for i in range(2, n):
            a,b = b, b+a
        return b

        
        
# @lc code=end

