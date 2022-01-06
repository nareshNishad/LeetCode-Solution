#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        str_length = len(needle)
        if str_length > len(haystack):
            return -1
        for i in range(len(haystack)-str_length+1):
            if haystack[i:str_length+i] == needle:
                return i
        return -1

        
# @lc code=end

