#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        for i in range(2, numRows+1):
            internal = []
            internal.append(1)
            pos  = 0
            while i -pos > 2:
                if out[i-2][pos+1]:
                    internal.append(out[i-2][pos]+out[i-2][pos+1])
                pos+=1
            internal.append(1)
            out.append(internal)
        return out


        
        
# @lc code=end

