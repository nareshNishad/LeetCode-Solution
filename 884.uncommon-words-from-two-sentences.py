#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
from collections import defaultdict


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(" "), s2.split(" ")
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        for i in s1:
            s1_dict[i] +=1
        for i in s2:
            s2_dict[i]+=1

        

        
# @lc code=end

