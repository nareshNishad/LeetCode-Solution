#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        possible = []
        for i in list1:
            if i in list2:
                possible.append(i)
        if len(possible) <= 1:
            return possible
        index_sum = list1.index(possible[0])+list2.index(possible[0])
        out = possible[0]
        for i in possible[1:]:
            if index_sum > list1.index(i)+list2.index(i):
                index_sum = list1.index(i)+list2.index(i)
                out = i
        print([out])
        return [out]
        
# @lc code=end

