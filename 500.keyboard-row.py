#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyborad = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        out = []
        
        # Naive method faster
        for i in words:
            temp = i.lower()
            for j in keyborad:
                if temp[0] in j:
                    for k in range(len(temp)):
                        if temp[k] not in j:
                            break
                        elif k == len(temp)-1:
                            out.append(i)
                    break           
        return out
        
        # Method 2(pythonic but slower beat only 5%)
        """
        for i in words:
            temp = i.lower()
            for j in keyborad:
                if temp[0] in j:
                    if set(temp) <= set(j):
                        out.append(i)
                    break           
        return out
        """

                  
# @lc code=end

