#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, j  in enumerate(numbers):
            if target - j in hashMap:
                return [hashMap[target-j]+1, i+1]
            hashMap[j] = i
        
# @lc code=end

