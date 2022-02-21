#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        out = 0
        for i, length in enumerate(height):
            for j, breath in enumerate(height[i:]):
                out = max(min(length, breath)*(j-i), out)
        return out


        
# @lc code=end

