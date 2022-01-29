#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for i in wordDict:
            if s.find(i) >= 0:
                s = s.replace(i, "")
            else:
                return False
        return True

        
# @lc code=end

