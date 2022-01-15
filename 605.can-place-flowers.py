#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        curr_one = flowerbed.count(1)
        if len(flowerbed)%2==0:
            return len(flowerbed)/2 - curr_one - n > 0
        return len(flowerbed)//2 - curr_one - n +1 >= 0


        
# @lc code=end

