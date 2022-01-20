#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        pre_index = -1
        for i in range(len(s)):
            if s[i] not in t[pre_index+1:]:
                return False
            pre_index = pre_index+t[pre_index+1:].index(s[i])+1
                    
        return True


        
# @lc code=end

