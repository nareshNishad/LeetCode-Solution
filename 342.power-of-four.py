#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and log(n,4).is_integer()
            
# @lc code=end

