#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return len(s)
        left =right=Max= 0
        while right < len(s):
            if s[right] in s[left:right]:
                left+=1
            else:
                right+=1
                Max = max(Max, right-left)
        return Max
# @lc code=end

