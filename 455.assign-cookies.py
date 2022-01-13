#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        for i in g:
            if i in s:
                s.pop(s.index(i))
                count+=1
        return count
        
# @lc code=end

