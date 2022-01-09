#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = 0
        t_sum = 0
        for i in range(len(s)):
            s_sum += ord(s[i])
        for j in range(len(t)):
            t_sum += ord(t[j])
        return chr(t_sum - s_sum)

        
# @lc code=end

