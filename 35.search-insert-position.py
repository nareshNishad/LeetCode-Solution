#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        # Without binery search
        """
        i = 0
        while i < len(nums) and nums[i] < target:
            if nums[i] == target:
                return i
            i+=1
        return i
        """
        left = 0
        right = len(nums) -1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        if nums[left] < target:
            return left +1
        else:
            return left
        
# @lc code=end

