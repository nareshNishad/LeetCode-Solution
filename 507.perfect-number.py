#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
from re import T


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        curr_sum = 0
        last_divide = 1
        for i in range(1,num//2+1, last_divide):
            if num%i==0:
                curr_sum+=i
                last_divide = i
            if curr_sum > num:
                return False
        if curr_sum == num:
            return True
        
# @lc code=end

