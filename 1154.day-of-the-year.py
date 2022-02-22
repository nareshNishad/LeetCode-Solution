#
# @lc app=leetcode id=1154 lang=python3
#
# [1154] Day of the Year
#

# @lc code=start
import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))
        d0 = datetime.date(year, month, day)
        d1 = datetime.date(year, 1, 1)
        return (d0- d1).days +1
        
# @lc code=end

