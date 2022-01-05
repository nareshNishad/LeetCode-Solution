#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        out = hashmap[s[-1]]
        for i in range(len(s)-1):
            if hashmap[s[i]] >= hashmap[s[i+1]]:
                out += hashmap[s[i]]
            else:
                out -= hashmap[s[i]]
        return out

        
# @lc code=end

