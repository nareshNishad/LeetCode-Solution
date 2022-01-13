#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Min_legth_str = min(strs, key=len)
        left = right = 0 
        Max = ""
        while right <= len(Min_legth_str):
            for i in strs:
                if i.find(Min_legth_str[left:right])!=0:
                    return max(Max, Min_legth_str[left:right-1], key=len)
            right+=1

        return max(Max, Min_legth_str[left:right], key=len)
                
        
# @lc code=end

