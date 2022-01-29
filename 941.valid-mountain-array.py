#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
from re import T


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[1] > arr[0]:
            increasing =True
        else:
            return False
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                increasing = False
            elif increasing and arr[i+1] <= arr[i]:
                return False
            elif not increasing and arr[i+1] >= arr[i]:
                return False
        return True and not increasing 
        
# @lc code=end

