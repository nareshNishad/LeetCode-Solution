#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lastChar = s[-1]
        for i in range(len(s)//2):
            if s[i] == lastChar:
                if s.replace(s[0:i+1],"") == "":
                    return True
                
                
        return False
        


        
# @lc code=end

