#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        visited = {}
        s = s.split(" ")
        pattern = list(pattern)
        if len(s) != len(pattern) or len(set(s))!= len(set(pattern)):
            return False
        for i in range(len(s)):
            if pattern[i] not in visited:
                visited[pattern[i]] = s[i]
            elif visited[pattern[i]] != s[i]:
                return False
        return True

        
# @lc code=end

