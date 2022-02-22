#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
from itertools import count


class Solution:
    def reverse(self, x: int) -> int:
        sign = [1,-1][x < 0]
        out = 0
        x = x*sign
        while x > 0:
            out = out*10 + x%10
            x = x// 10
        return 0 if out > pow(2, 31) else out*sign
        
# @lc code=end

