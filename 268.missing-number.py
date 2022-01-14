#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_till_n = n*(n+1)//2
        nums_sum = sum(nums)
        return sum_till_n - nums_sum
        
        
# @lc code=end

