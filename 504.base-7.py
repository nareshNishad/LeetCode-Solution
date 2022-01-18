#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        n = abs(num)
        while n > 0:
            res = str(n % 7) + res
            n //= 7
        return "-" * (num < 0) + res or "0"
        
# @lc code=end

