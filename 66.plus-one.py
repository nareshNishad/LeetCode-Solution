#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits) - 1
        while length >= 0 and digits[length]+1>9:
            digits[length] = 0
            length -=1
        if length < 0:
            digits.insert(0, 1)
        else:
            digits[length] += 1
        return digits





        
# @lc code=end

