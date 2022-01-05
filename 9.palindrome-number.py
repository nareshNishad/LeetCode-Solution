#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x <= 9:
            return True
        else:
            out = 0
            input_num = x
            while(x>0):
                last_digit = x % 10 
                out = out*10 + last_digit
                x = x // 10
            if out == input_num:
                return True
            else:
                return False



        
# @lc code=end

