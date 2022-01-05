#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        Length = len(s)
        if Length == 0:
            return True
        if Length % 2 != 0:
            return False
        
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if not stack or d[stack.pop()] != i:
                    return False
        if len(stack) == 0:
            return True




        
        
# @lc code=end

