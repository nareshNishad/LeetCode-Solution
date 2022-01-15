#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for i in range(len(s)):
            s_dict[s[i]] += 1
        for i in range(len(t)):
            t_dict[t[i]] += 1
        if s_dict == t_dict:
            return True
        return False
        

        
        
# @lc code=end

