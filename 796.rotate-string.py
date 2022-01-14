#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
import re


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        first_occ = goal.index(s[0])
        remaining = len(goal) - first_occ
        print(s[0: remaining], goal[remaining+1:] , s[remaining:], goal[0:remaining+1])
        if remaining+1==len(goal) and s[0: remaining] == goal[:remaining+1] and s[remaining:] == goal[remaining+1:]:
            return True
        elif s[0: remaining]== goal[remaining+1:] and s[remaining:]== goal[0:remaining+1]:
            return True

        return False
        
# @lc code=end

