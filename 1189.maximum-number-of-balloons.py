#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashMap = {}
        for i in range(len(text)):
            if text[i] in "balloon":
                hashMap[text[i]] = hashMap.get(text[i], 0)+1
        if len(hashMap) <5:
            return 0
        bna_Min = min(hashMap['b'], hashMap['n'], hashMap['a'])
        lo_min = min(hashMap['l'], hashMap['o'])//2
        return min(bna_Min, lo_min) 
        

            
        
# @lc code=end

