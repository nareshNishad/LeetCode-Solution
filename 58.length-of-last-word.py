#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        Length = len(s)-1
        for i in range(Length, -1, -1):
            if s[i] == " ":
                return Length -i 
        return Length + 1
        
# @lc code=end

