#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
#def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high=0, n+1
        while(low<high):
            m=(low+high)//2
            if guess(m)>0:    low=m+1
            elif guess(m)<0:    high=m
            else:    return m

        
# @lc code=end

