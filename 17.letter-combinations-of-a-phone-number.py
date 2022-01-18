#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        input_map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",
        "7":"pqrs","8":"tuv","9":"wxyz"}
        out = [""]
        for i in range(len(digits)):
            out = [x + y for x, y in product(out, input_map[digits[i]])]
        return out
        

        
# @lc code=end

