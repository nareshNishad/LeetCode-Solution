#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <=1:
            return s
        out = ""
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                if s[i:j] == s[i:j][::-1] and len(out) < len(s[i:j]):
                    out = s[i:j]
        return out
        
# @lc code=end

