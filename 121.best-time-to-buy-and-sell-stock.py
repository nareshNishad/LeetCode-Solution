#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max = 0
        Buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i] - Buy < 0:
                Buy = prices[i]
            elif prices[i] - Buy > Max:
                Max = prices[i] - Buy

        return Max

        
# @lc code=end

