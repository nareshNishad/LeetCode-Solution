#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        if x == 1 :
            return 1
        for i in range((x//2)+1):
            if i*i==x or (i*i <x and (i+1)*(i+1) > x):
                return i
        """
        # Binery search
        left = 1
        right = x
        while left <= right:
            mid = left + (right -left)//2
            if mid*mid > x:
                right = mid-1
            elif mid*mid < x:
                left = mid +1
            else:
                return mid
        return right

        
# @lc code=end

