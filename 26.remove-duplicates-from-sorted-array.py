#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[count ] = nums[i+1]
                count+=1
        
        return count
        



        
# @lc code=end

