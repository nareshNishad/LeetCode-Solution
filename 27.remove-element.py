#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        # Pop method
        # Slow Beat only 5%
        """
        while count < len(nums):
            if nums[count] == val:
                nums.pop(count)
                count -= 1
            count +=1
        return len(nums) 
        """
        #Fast beat 92%
        for i in nums:
            if i != val:
                nums[count] = i
                count+=1
        return count
        
# @lc code=end

