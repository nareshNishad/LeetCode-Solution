#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        curr = head
        while curr:
            if curr.next in visited:
                return True
            else:
                visited.append(curr.next)
            curr = curr.next
        return False
        
# @lc code=end

